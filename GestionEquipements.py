from PySide6.QtSql import QSqlQuery

class GestionEquipements:
    def __init__(self, db_connection):
        self.db = db_connection

    def ajouter_equipement(self, type_equip, marque, modele, numero_serie, etat, nom_utilisateur):
        """Ajoute un équipement à la base de données"""
        try:
            # Vérifier si on utilise Qt ou pymysql
            if hasattr(self.db, 'use_qt_mysql') and self.db.use_qt_mysql:
                return self._ajouter_avec_qt(type_equip, marque, modele, numero_serie, etat, nom_utilisateur)
            else:
                return self._ajouter_avec_pymysql(type_equip, marque, modele, numero_serie, etat, nom_utilisateur)
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'équipement: {e}")
            return False

    def _ajouter_avec_qt(self, type_equip, marque, modele, numero_serie, etat, nom_utilisateur):
        """Ajoute un équipement avec Qt"""
        query = QSqlQuery(self.db.db)
        query.prepare("""
            INSERT INTO equipements (type, marque, modele, numero_serie, etat, nom_utilisateur)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(type_equip)
        query.addBindValue(marque)
        query.addBindValue(modele)
        query.addBindValue(numero_serie)
        query.addBindValue(etat)
        query.addBindValue(nom_utilisateur)

        if query.exec():
            return True
        else:
            print(f"Erreur Qt: {query.lastError().text()}")
            return False

    def _ajouter_avec_pymysql(self, type_equip, marque, modele, numero_serie, etat, nom_utilisateur):
        """Ajoute un équipement avec pymysql"""
        try:
            with self.db.mysql_connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO equipements (type, marque, modele, numero_serie, etat, nom_utilisateur)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (type_equip, marque, modele, numero_serie, etat, nom_utilisateur))
            self.db.mysql_connection.commit()
            return True
        except Exception as e:
            print(f"Erreur pymysql: {e}")
            return False

    def lister_equipements(self):
        """Récupère la liste des équipements"""
        try:
            # Vérifier si on utilise Qt ou pymysql
            if hasattr(self.db, 'use_qt_mysql') and self.db.use_qt_mysql:
                return self._lister_avec_qt()
            else:
                return self._lister_avec_pymysql()
        except Exception as e:
            print(f"Erreur lors de la récupération des équipements: {e}")
            return []

    def _lister_avec_qt(self):
        """Liste les équipements avec Qt"""
        equipements = []
        query = QSqlQuery("SELECT * FROM equipements ORDER BY id", self.db.db)

        while query.next():
            equipement = {
                'id': query.value(0),
                'type': query.value(1),
                'marque': query.value(2),
                'modele': query.value(3),
                'numero_serie': query.value(4),
                'etat': query.value(5),
                'nom_utilisateur': query.value(6)
            }
            equipements.append(equipement)

        return equipements

    def _lister_avec_pymysql(self):
        """Liste les équipements avec pymysql"""
        try:
            with self.db.mysql_connection.cursor() as cursor:
                cursor.execute("SELECT * FROM equipements ORDER BY id")
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur pymysql: {e}")
            return []

    def supprimer_equipement(self, id_equipement):
        """Supprime un équipement"""
        try:
            if hasattr(self.db, 'use_qt_mysql') and self.db.use_qt_mysql:
                return self._supprimer_avec_qt(id_equipement)
            else:
                return self._supprimer_avec_pymysql(id_equipement)
        except Exception as e:
            print(f"Erreur lors de la suppression: {e}")
            return False

    def _supprimer_avec_qt(self, id_equipement):
        """Supprime avec Qt"""
        query = QSqlQuery(self.db.db)
        query.prepare("DELETE FROM equipements WHERE id = ?")
        query.addBindValue(id_equipement)
        return query.exec()

    def _supprimer_avec_pymysql(self, id_equipement):
        """Supprime avec pymysql"""
        try:
            with self.db.mysql_connection.cursor() as cursor:
                cursor.execute("DELETE FROM equipements WHERE id = %s", (id_equipement,))
            self.db.mysql_connection.commit()
            return True
        except Exception as e:
            print(f"Erreur pymysql: {e}")
            return False
