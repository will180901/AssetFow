import bcrypt
import re
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QRect, QSize # QSize n'est pas utilisé directement ici, mais souvent utile
from PySide6.QtGui import QPainter, QPainterPath, QColor, QBrush
from ui_fen_enreg_utilisateur import Ui_fen_enreg_utilisateur

class DialogEnregUtilisateur(QDialog):
    def __init__(self, gestion_utilisateurs, parent=None):
        super().__init__(parent)
        self.ui = Ui_fen_enreg_utilisateur()
        self.ui.setupUi(self)

        # On garde une référence à notre gestionnaire d'utilisateurs
        self.gestion_utilisateurs = gestion_utilisateurs

        # On cache le message d'erreur au début
        self.ui.label_affiche_erreur_validation.setText("")

        # Effet visuel sur le QDialog d'ajout utilisateur (DialogEnregUtilisateur)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Définir un rayon pour les bords arrondis
        self.border_radius = 15

        # Remplir le ComboBox avec les rôles disponibles
        self.initialiser_roles()

        # Connecter les boutons aux méthodes
        self.ui.btn_creer_ajout_utilisateur.clicked.connect(self.creer_utilisateur)
        # On connecte le bouton Annuler à self.reject() pour fermer la fenêtre en signalant une annulation
        self.ui.btn_annuler_ajout_utilisateur.clicked.connect(self.reject)

        # Connecter les champs de saisie pour effacer le message d'erreur dès qu'on y touche
        self.ui.lineEdit_nom_complet_utilisateur.textChanged.connect(self.effacer_erreur)
        self.ui.lineEdit_email_utilisateur.textChanged.connect(self.effacer_erreur)
        self.ui.lineEdit_mot_de_passe.textChanged.connect(self.effacer_erreur)
        self.ui.lineEdit_confirmation_mot_de_passe.textChanged.connect(self.effacer_erreur)
        self.ui.comboBox_role_utilisateur.currentIndexChanged.connect(self.effacer_erreur) # Aussi pour le combobox

    def initialiser_roles(self):
        """Ajoute les rôles prédéfinis dans le QComboBox."""
        roles = ["utilisateur", "administrateur", "technicien"]
        self.ui.comboBox_role_utilisateur.addItems(roles)

    def effacer_erreur(self):
        """Efface le texte du label d'erreur de validation."""
        self.ui.label_affiche_erreur_validation.setText("")

    def valider_saisies(self, nom, email, mot_de_passe, confirmation_mdp):
        """
        Valide tous les champs de saisie et retourne True si tout est bon, False sinon.
        Met à jour le label d'erreur en cas de problème.
        """
        if not all([nom, email, mot_de_passe, confirmation_mdp]):
            self.ui.label_affiche_erreur_validation.setText("Tous les champs sont obligatoires.")
            return False

        # Validation du nom
        if nom.isdigit(): # Vérifie si le nom est composé uniquement de chiffres
            self.ui.label_affiche_erreur_validation.setText("Le nom ne peut pas être composé uniquement de chiffres.")
            return False
        if nom and nom[0].isdigit(): # Vérifie si le premier caractère est un chiffre
            self.ui.label_affiche_erreur_validation.setText("Le nom ne peut pas commencer par un chiffre.")
            return False

        # Validation de l'email
        # Expression régulière pour un email basique (nom@domaine.ext)
        # C'est une validation simple, tu peux la rendre plus complexe si besoin.
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|fr|org|net|io|co|ai|cloud|gmail|icloud|outlook|yahoo|hotmail)$", email):
            self.ui.label_affiche_erreur_validation.setText("Format d'email invalide (ex: nom@domaine.com).")
            return False

        # Vérifier si l'email existe déjà dans la base de données
        if self.gestion_utilisateurs.email_existe(email):
            self.ui.label_affiche_erreur_validation.setText("Cette adresse e-mail est déjà utilisée.")
            return False

        # Validation du mot de passe
        if len(mot_de_passe) < 8:
            self.ui.label_affiche_erreur_validation.setText("Le mot de passe doit avoir au moins 8 caractères.")
            return False
        if not any(char.isupper() for char in mot_de_passe):
            self.ui.label_affiche_erreur_validation.setText("Le mot de passe doit contenir au moins une majuscule.")
            return False
        # Tu peux ajouter d'autres validations ici si tu veux (chiffres, caractères spéciaux, etc.)

        if mot_de_passe != confirmation_mdp:
            self.ui.label_affiche_erreur_validation.setText("Les mots de passe ne correspondent pas.")
            return False

        return True # Toutes les validations sont passées

    def creer_utilisateur(self):
        """
        Valide les données, hache le mot de passe et l'ajoute à la base de données.
        """
        nom = self.ui.lineEdit_nom_complet_utilisateur.text().strip()
        email = self.ui.lineEdit_email_utilisateur.text().strip()
        mot_de_passe = self.ui.lineEdit_mot_de_passe.text()
        confirmation_mdp = self.ui.lineEdit_confirmation_mot_de_passe.text()
        role = self.ui.comboBox_role_utilisateur.currentText()

        # --- Validation des données ---
        if not self.valider_saisies(nom, email, mot_de_passe, confirmation_mdp):
            return # Si les saisies ne sont pas valides, on s'arrête ici

        # --- Hachage du mot de passe avec bcrypt ---
        try:
            # On encode le mot de passe en bytes (UTF-8)
            password_bytes = mot_de_passe.encode('utf-8')
            # On génère un "sel" pour renforcer le hachage
            salt = bcrypt.gensalt()
            # On hache le mot de passe
            hashed_password = bcrypt.hashpw(password_bytes, salt)
            # On décode le hash en string pour le stocker en BDD
            hashed_password_str = hashed_password.decode('utf-8')

        except Exception as e:
            QMessageBox.critical(self, "Erreur de hachage", f"Impossible de sécuriser le mot de passe : {e}")
            return


        # --- Ajout à la base de données ---
        if self.gestion_utilisateurs.ajouter_utilisateur(nom, email, hashed_password_str, role):
            QMessageBox.information(self, "Succès", f"L'utilisateur '{nom}' a été créé avec succès.")
            self.accept() # self.accept() ferme la fenêtre et envoie un signal de succès (Dialog.Accepted)
        else:
            # Si l'ajout échoue dans GestionUtilisateur (par ex. problème BDD),
            # un message d'erreur est déjà affiché là-bas, on peut juste mettre un message générique ici.
            self.ui.label_affiche_erreur_validation.setText("Une erreur est survenue lors de l'ajout de l'utilisateur.")

    def paintEvent(self, event):
        """
        Surcharge la méthode paintEvent pour dessiner un fond arrondi.
        Cette méthode est appelée par Qt chaque fois que la fenêtre doit être redessinée.
        """
        painter = QPainter(self)
        # Active l'anti-crénelage pour des bords plus lisses
        painter.setRenderHint(QPainter.Antialiasing)

        # Définit la couleur de fond de la fenêtre. Ici, blanc opaque.
        # Tu peux changer cette couleur pour qu'elle corresponde à ton design.
        brush = QBrush(QColor(255, 255, 255))
        painter.setBrush(brush)
        # Pas de bordure pour la forme que l'on dessine
        painter.setPen(Qt.NoPen)

        # Crée un chemin de dessin
        path = QPainterPath()
        # Définit le rectangle de la fenêtre (0,0) au coin inférieur droit
        rect = QRect(0, 0, self.width(), self.height())
        # Ajoute un rectangle arrondi au chemin
        path.addRoundedRect(rect, self.border_radius, self.border_radius)
        # Dessine le chemin sur la fenêtre
        painter.drawPath(path)

    def resizeEvent(self, event):
        """
        Surcharge la méthode resizeEvent pour redimensionner le masque
        de la région et garantir des bords arrondis lors du redimensionnement.
        """
        # Recrée le chemin avec les nouvelles dimensions de la fenêtre
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, self.border_radius, self.border_radius)

        # Applique le masque à la fenêtre. Seule la zone définie par le chemin sera visible.
        self.setMask(path.toFillPolygon().toPolygon())

        # Appelle l'implémentation de base pour que le redimensionnement normal fonctionne
        super().resizeEvent(event)
