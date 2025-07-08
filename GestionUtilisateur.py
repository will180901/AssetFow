from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QMessageBox

class GestionUtilisateur:
    def __init__(self, db):
        self.db = db

    def ajouter_utilisateur(self, nom, email, mot_de_passe, role=None):
        """Ajoute un nouvel utilisateur"""
        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO utilisateurs (nom, email, mot_de_passe, role)
            VALUES (?, ?, ?, ?)
        """)
        query.addBindValue(nom)
        query.addBindValue(email)
        query.addBindValue(mot_de_passe)
        query.addBindValue(role)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur d'ajout", f"Impossible d'ajouter l'utilisateur:\n{error}")
            return False
        return True

    def modifier_utilisateur(self, id_utilisateur, nom=None, email=None, mot_de_passe=None, role=None):
        """Modifie un utilisateur existant"""
        # Construire la requête dynamiquement selon les champs à modifier
        champs = []
        valeurs = []

        if nom is not None:
            champs.append("nom = ?")
            valeurs.append(nom)
        if email is not None:
            champs.append("email = ?")
            valeurs.append(email)
        if mot_de_passe is not None:
            champs.append("mot_de_passe = ?")
            valeurs.append(mot_de_passe)
        if role is not None:
            champs.append("role = ?")
            valeurs.append(role)

        if not champs:
            QMessageBox.warning(None, "Avertissement", "Aucune modification à effectuer")
            return False

        query = QSqlQuery(self.db)
        requete = f"UPDATE utilisateurs SET {', '.join(champs)} WHERE id = ?"
        query.prepare(requete)

        for valeur in valeurs:
            query.addBindValue(valeur)
        query.addBindValue(id_utilisateur)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de modification", f"Impossible de modifier l'utilisateur:\n{error}")
            return False
        return True

    def supprimer_utilisateur(self, id_utilisateur):
        """Supprime un utilisateur"""
        query = QSqlQuery(self.db)
        query.prepare("DELETE FROM utilisateurs WHERE id = ?")
        query.addBindValue(id_utilisateur)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de suppression", f"Impossible de supprimer l'utilisateur:\n{error}")
            return False
        return True

    def lister_utilisateurs(self):
        """Retourne tous les utilisateurs"""
        query = QSqlQuery(self.db)
        query.exec("SELECT * FROM utilisateurs ORDER BY nom")

        utilisateurs = []
        while query.next():
            utilisateurs.append({
                'id': query.value(0),
                'nom': query.value(1),
                'email': query.value(2),
                'mot_de_passe': query.value(3),
                'role': query.value(4)
            })
        return utilisateurs

    def rechercher_utilisateur(self, critere, valeur):
        """Recherche un utilisateur par critère"""
        query = QSqlQuery(self.db)
        query.prepare(f"SELECT * FROM utilisateurs WHERE {critere} = ?")
        query.addBindValue(valeur)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de recherche", f"Erreur lors de la recherche:\n{error}")
            return None

        if query.next():
            return {
                'id': query.value(0),
                'nom': query.value(1),
                'email': query.value(2),
                'mot_de_passe': query.value(3),
                'role': query.value(4)
            }
        return None

    def verifier_connexion(self, email, mot_de_passe):
        """Vérifie les identifiants de connexion"""
        utilisateur = self.rechercher_utilisateur('email', email)
        if utilisateur and utilisateur['mot_de_passe'] == mot_de_passe:
            return utilisateur
        return None

    def email_existe(self, email):
        """Vérifie si un email existe déjà"""
        return self.rechercher_utilisateur('email', email) is not None
