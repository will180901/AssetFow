from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QWidget
from ui_fen_modifier_utilisateur import Ui_fen_modifier_utilisateur

class FenModifierUtilisateur(QDialog):
    def __init__(self, utilisateur, gestion_utilisateurs, parent=None):
        super().__init__(parent)
        self.ui = Ui_fen_modifier_utilisateur()
        self.ui.setupUi(self)
        self.utilisateur = utilisateur
        self.gestion_utilisateurs = gestion_utilisateurs
        self.erreur = None
        self._remplir_combo()
        self._connect_signaux()
        self.ui.label_affiche_erreur_validation.setText("")
        self.ui.lineEdit_champs_de_modification.setText("")
        self.ui.label_valeur_actuelle_a_modifier.setText("")
        # Bouton annuler
        if hasattr(self.ui, 'btn_annuler_modification_utilisateur'):
            self.ui.btn_annuler_modification_utilisateur.clicked.connect(self._annuler_et_fermer)

    def _remplir_combo(self):
        # On ne propose pas le mot de passe
        champs = [
            ("Nom complet", "nom"),
            ("Email", "email"),
            ("Rôle", "role")
        ]
        self.champs = champs
        self.ui.comboBox_choix_de_modification.clear()
        for label, key in champs:
            self.ui.comboBox_choix_de_modification.addItem(label, key)
        self.ui.comboBox_choix_de_modification.setCurrentIndex(0)
        self._maj_valeur_actuelle()

    def _connect_signaux(self):
        self.ui.comboBox_choix_de_modification.currentIndexChanged.connect(self._maj_valeur_actuelle)
        self.ui.lineEdit_champs_de_modification.textChanged.connect(self._vider_erreur)
        self.ui.comboBox_choix_de_modification.activated.connect(self._vider_erreur)
        self.ui.btn_valider_modification_utilisateur.clicked.connect(self._valider_modification)

    def _maj_valeur_actuelle(self):
        key = self.ui.comboBox_choix_de_modification.currentData()
        valeur = self.utilisateur.get(key, "")
        self.ui.label_valeur_actuelle_a_modifier.setText(str(valeur))
        self.ui.lineEdit_champs_de_modification.setText("")
        self._vider_erreur()

    def _vider_erreur(self):
        self.ui.label_affiche_erreur_validation.setText("")

    def _valider_modification(self):
        key = self.ui.comboBox_choix_de_modification.currentData()
        nouvelle_valeur = self.ui.lineEdit_champs_de_modification.text().strip()
        if not nouvelle_valeur:
            self.ui.label_affiche_erreur_validation.setText("Le champ ne peut pas être vide.")
            return
        # Validation selon le champ
        if key == "email":
            if not self.gestion_utilisateurs.valider_email(nouvelle_valeur):
                self.ui.label_affiche_erreur_validation.setText("Email invalide.")
                return
        elif key == "nom":
            if not self.gestion_utilisateurs.valider_nom(nouvelle_valeur):
                self.ui.label_affiche_erreur_validation.setText("Nom invalide.")
                return
        elif key == "role":
            if not self.gestion_utilisateurs.valider_role(nouvelle_valeur):
                self.ui.label_affiche_erreur_validation.setText("Rôle invalide.")
                return
        # Si tout est bon, on met à jour
        if not self.gestion_utilisateurs.modifier_utilisateur(self.utilisateur['id'], key, nouvelle_valeur):
            self.ui.label_affiche_erreur_validation.setText("Erreur lors de la modification.")
            return
        self.accept()

    def showEvent(self, event):
        super().showEvent(event)
        # Crée un overlay noir flou couvrant tout le parent (fen_main)
        if self.parent():
            self._overlay = QWidget(self.parent())
            self._overlay.setStyleSheet('background-color: rgba(0,0,0,0.35); backdrop-filter: blur(8px);')
            self._overlay.setGeometry(self.parent().rect())
            self._overlay.show()
            self._overlay.raise_()
            self.raise_()

    def closeEvent(self, event):
        # Nettoie l'overlay si présent
        if hasattr(self, '_overlay') and self._overlay:
            self._overlay.hide()
            self._overlay.deleteLater()
            self._overlay = None
        super().closeEvent(event)

    def reject(self):
        # Ferme la fenêtre et retire l'overlay via le mécanisme natif de QDialog
        super().reject()

    def _annuler_et_fermer(self):
        # Retire d'abord le rideau, puis ferme la boîte de dialogue
        if hasattr(self, '_overlay') and self._overlay:
            self._overlay.hide()
            self._overlay.deleteLater()
            self._overlay = None
        super().reject()
