from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox
import pymysql

class GestionBD:
    def __init__(self, host="localhost", user="root", password="", db_name="AssetFlow", replace=False):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.replace = replace

        # Tentative d'utilisation de QMYSQL
        self.use_qt_mysql = False
        self.mysql_connection = None
        self._db = None

        # Vérifier si QMYSQL est disponible
        available_drivers = QSqlDatabase.drivers()
        print("Pilotes disponibles :", available_drivers)

        if "QMYSQL" in available_drivers:
            print("Pilote Qt MySQL disponible")
            self.use_qt_mysql = True
            self._db = QSqlDatabase.addDatabase("QMYSQL")
            self._db.setHostName(host)
            self._db.setUserName(user)
            self._db.setPassword(password)
            self._db.setDatabaseName(db_name)
        else:
            print("Utilisation de pymysql comme alternative")
            self.use_qt_mysql = False

    def ouvrir_base_de_donnees(self):
        """Ouvre la connexion à la base de données MySQL"""
        print(f"Tentative de connexion à MySQL: {self.user}@{self.host}/{self.db_name}")

        if self.use_qt_mysql:
            return self._ouvrir_avec_qt()
        else:
            return self._ouvrir_avec_pymysql()

    def _ouvrir_avec_qt(self):
        """Ouvre la connexion avec Qt MySQL"""
        try:
            if not self._db.open():
                error = self._db.lastError().text()
                print(f"Erreur Qt MySQL: {error}")
                # Fallback vers pymysql
                self.use_qt_mysql = False
                return self._ouvrir_avec_pymysql()
            print("Connexion Qt MySQL réussie")
            return True
        except Exception as e:
            print(f"Exception Qt MySQL: {e}")
            # Fallback vers pymysql
            self.use_qt_mysql = False
            return self._ouvrir_avec_pymysql()

    def _ouvrir_avec_pymysql(self):
        """Ouvre la connexion avec pymysql"""
        try:
            # Tentative de connexion
            self.mysql_connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            print("Connexion pymysql réussie")
            return True

        except pymysql.Error as e:
            error_msg = f"Erreur MySQL ({e.args[0]}): {e.args[1]}"
            print(error_msg)

            # Essayer de créer la base de données si elle n'existe pas
            if e.args[0] == 1049:  # Unknown database
                return self._creer_base_de_donnees()
            else:
                QMessageBox.critical(
                    None,
                    "Erreur de connexion MySQL",
                    f"Impossible de se connecter à MySQL:\n{error_msg}\n\n"
                    "Vérifiez que :\n"
                    "• MySQL Server est démarré\n"
                    "• Les identifiants sont corrects\n"
                    "• Le port 3306 est ouvert"
                )
                return False

        except Exception as e:
            QMessageBox.critical(
                None,
                "Erreur de connexion",
                f"Erreur inattendue:\n{str(e)}"
            )
            return False

    def _creer_base_de_donnees(self):
        """Crée la base de données si elle n'existe pas"""
        try:
            print(f"Tentative de création de la base de données '{self.db_name}'")

            # Connexion sans spécifier de base de données
            temp_connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                charset='utf8mb4'
            )

            with temp_connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

            temp_connection.commit()
            temp_connection.close()

            print(f"Base de données '{self.db_name}' créée avec succès")

            # Maintenant se connecter à la nouvelle base
            return self._ouvrir_avec_pymysql()

        except Exception as e:
            QMessageBox.critical(
                None,
                "Erreur de création de base",
                f"Impossible de créer la base de données:\n{str(e)}"
            )
            return False

    def creer_tables(self):
        """Crée les tables avec leurs contraintes pour MySQL"""
        print("Création des tables...")

        if self.use_qt_mysql:
            return self._creer_tables_qt()
        else:
            return self._creer_tables_pymysql()

    def _creer_tables_qt(self):
        """Crée les tables avec Qt MySQL"""
        requetes = self._get_requetes_creation()

        query = QSqlQuery(self._db)
        for nom_table, requete in requetes.items():
            print(f"Création de la table: {nom_table}")
            if not query.exec(requete):
                error = query.lastError().text()
                QMessageBox.critical(
                    None,
                    "Erreur SQL Qt",
                    f"Erreur création table {nom_table}:\n{error}"
                )
                return False
        print("Tables créées avec succès (Qt)")
        return True

    def _creer_tables_pymysql(self):
        """Crée les tables avec pymysql"""
        requetes = self._get_requetes_creation()

        try:
            with self.mysql_connection.cursor() as cursor:
                for nom_table, requete in requetes.items():
                    print(f"Création de la table: {nom_table}")
                    cursor.execute(requete)
            self.mysql_connection.commit()
            print("Tables créées avec succès (pymysql)")
            return True
        except Exception as e:
            QMessageBox.critical(
                None,
                "Erreur SQL pymysql",
                f"Erreur création table:\n{str(e)}"
            )
            return False

    def _get_requetes_creation(self):
        """Retourne les requêtes de création des tables"""
        return {
            "utilisateurs": """
                CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nom VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    mot_de_passe VARCHAR(255) NOT NULL,
                    role VARCHAR(50) DEFAULT 'utilisateur',
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """,

            "tickets": """
                CREATE TABLE IF NOT EXISTS tickets (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    sujet VARCHAR(255) NOT NULL,
                    description TEXT,
                    statut ENUM('ouvert', 'ferme', 'en_cours') DEFAULT 'ouvert',
                    priorite ENUM('faible', 'moyenne', 'elevee') DEFAULT 'moyenne',
                    nom_utilisateur VARCHAR(100),
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """,

            "equipements": """
                CREATE TABLE IF NOT EXISTS equipements (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    type VARCHAR(100) NOT NULL,
                    marque VARCHAR(100),
                    modele VARCHAR(100),
                    numero_serie VARCHAR(100) UNIQUE,
                    etat ENUM('en_service', 'hors_service', 'en_stock', 'en_reparation') DEFAULT 'en_stock',
                    nom_utilisateur VARCHAR(100),
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """
        }

    def fermer_base_de_donnees(self):
        """Ferme la connexion à la base de données"""
        try:
            if self.use_qt_mysql:
                if hasattr(self, '_db') and self._db and self._db.isOpen():
                    self._db.close()
                    print("Connexion Qt MySQL fermée")
            else:
                if self.mysql_connection:
                    self.mysql_connection.close()
                    print("Connexion pymysql fermée")
        except Exception as e:
            print(f"Erreur lors de la fermeture: {e}")

    def __del__(self):
        """Destructeur - ferme automatiquement la connexion"""
        self.fermer_base_de_donnees()

    def execute_query(self, query_str, params=None):
        """Exécute une requête SQL"""
        if self.use_qt_mysql:
            return self._execute_query_qt(query_str, params)
        else:
            return self._execute_query_pymysql(query_str, params)

    def _execute_query_qt(self, query_str, params=None):
        """Exécute une requête avec Qt"""
        query = QSqlQuery(self._db)
        if params:
            query.prepare(query_str)
            for param in params:
                query.addBindValue(param)
            query.exec()
        else:
            query.exec(query_str)

        # Récupérer les résultats
        results = []
        while query.next():
            record = {}
            for i in range(query.record().count()):
                field_name = query.record().fieldName(i)
                record[field_name] = query.value(i)
            results.append(record)
        return results

    def _execute_query_pymysql(self, query_str, params=None):
        """Exécute une requête avec pymysql"""
        try:
            with self.mysql_connection.cursor() as cursor:
                cursor.execute(query_str, params)
                if query_str.strip().upper().startswith('SELECT'):
                    return cursor.fetchall()
                else:
                    self.mysql_connection.commit()
                    return cursor.rowcount
        except Exception as e:
            print(f"Erreur lors de l'exécution de la requête: {e}")
            return None

    @property
    def db(self):
        """Propriété pour compatibilité"""
        if self.use_qt_mysql:
            return self._db
        else:
            return self  # Retourner self pour que les méthodes pymysql fonctionnent

    @db.setter
    def db(self, value):
        """Setter pour la propriété db"""
        if self.use_qt_mysql:
            self._db = value
