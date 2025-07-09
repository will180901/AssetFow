# Nom du fichier : GestionUtilisateur.py

# On utilise les imports de PySide6
# from PySide6.QtSql import QSqlQuery # Plus besoin d'importer QSqlQuery ici
from PySide6.QtWidgets import QMessageBox

class GestionUtilisateur:
    def __init__(self, db_manager): # On renomme pour plus de clarté
        self.db_manager = db_manager # On garde une référence au GestionBD complet

    def ajouter_utilisateur(self, nom, email, mot_de_passe_hache, role=None):
        """Ajoute un nouvel utilisateur avec un mot de passe déjà haché"""
        query_str = """
            INSERT INTO utilisateurs (nom, email, mot_de_passe, role)
            VALUES (%s, %s, %s, %s)
        """
        params = (nom, email, mot_de_passe_hache, role)

        # On utilise la méthode execute_query du gestionnaire de BDD
        result = self.db_manager.execute_query(query_str, params)

        if result is None: # Si execute_query renvoie None, il y a eu une erreur
            # L'erreur est déjà affichée par GestionBD
            return False
        return True

    def modifier_utilisateur(self, id_utilisateur, nom=None, email=None, mot_de_passe=None, role=None):
        """Modifie un utilisateur existant"""
        champs = []
        valeurs = []

        if nom is not None:
            champs.append("nom = %s") # Utiliser %s pour pymysql
            valeurs.append(nom)
        if email is not None:
            champs.append("email = %s")
            valeurs.append(email)
        if mot_de_passe is not None:
            champs.append("mot_de_passe = %s")
            valeurs.append(mot_de_passe)
        if role is not None:
            champs.append("role = %s")
            valeurs.append(role)

        if not champs:
            QMessageBox.warning(None, "Avertissement", "Aucune modification à effectuer")
            return False

        requete = f"UPDATE utilisateurs SET {', '.join(champs)} WHERE id = %s"
        valeurs.append(id_utilisateur)

        result = self.db_manager.execute_query(requete, tuple(valeurs)) # Convertir en tuple pour pymysql

        if result is None:
            return False
        return True

    def supprimer_utilisateur(self, id_utilisateur):
        """Supprime un utilisateur"""
        query_str = "DELETE FROM utilisateurs WHERE id = %s"
        params = (id_utilisateur,)

        result = self.db_manager.execute_query(query_str, params)

        if result is None:
            return False
        return True

    def lister_utilisateurs(self):
        """Retourne tous les utilisateurs"""
        query_str = "SELECT id, nom, email, role FROM utilisateurs ORDER BY nom" # On ne récupère pas le mot de passe haché directement
        utilisateurs_raw = self.db_manager.execute_query(query_str)

        if utilisateurs_raw is None:
            return [] # En cas d'erreur, retourne une liste vide

        # Assurez-vous que les résultats sont bien formatés en dictionnaire
        # (execute_query de GestionBD le fait déjà avec DictCursor pour pymysql)
        return utilisateurs_raw

    def rechercher_utilisateur(self, critere, valeur):
        """Recherche un utilisateur par critère"""
        query_str = f"SELECT id, nom, email, mot_de_passe, role FROM utilisateurs WHERE {critere} = %s"
        params = (valeur,)

        result = self.db_manager.execute_query(query_str, params)

        if result and len(result) > 0:
            return result[0] # Renvoie le premier résultat trouvé
        return None

    def verifier_connexion(self, email, mot_de_passe):
        """Vérifie les identifiants de connexion"""
        utilisateur = self.rechercher_utilisateur('email', email)
        if utilisateur:
            # Ici, tu devras utiliser bcrypt.checkpw pour vérifier le mot de passe
            # C'est mieux de faire ça dans une fonction de connexion spécifique
            # plutôt que de comparer directement le hash.
            # Pour l'instant, je laisse la logique simplifiée, mais c'est une amélioration à faire.
            if bcrypt.checkpw(mot_de_passe.encode('utf-8'), utilisateur['mot_de_passe'].encode('utf-8')):
                 return utilisateur
        return None

    def email_existe(self, email):
        """Vérifie si un email existe déjà"""
        return self.rechercher_utilisateur('email', email) is not None
