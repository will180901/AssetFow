# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_form import Ui_fen_main
from NavigationManager import NavigationManager
from GestionBD import GestionBD

class fen_main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fen_main()
        self.ui.setupUi(self)

        self.navigation_manager = NavigationManager(self.ui)
        self.navigation_manager.show_page(self.ui.page_tableau_de_bord)


        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "motdepasse",  # Changez ceci
            "db_name": "test",
            "replace": False
        }

        # Initialisation de la base de données
        self.init_database()

        # Connecter le bouton d'ajout d'équipement
        self.ui.btn_ajouter_equipement.clicked.connect(self.ajouter_equipement)

        # Initialiser le tableau des équipements
        self.actualiser_tableau_equipements()

    def init_database(self):
        """Initialise la connexion à la base de données"""
        try:
            self.gestion_bd = GestionBD(**self.db_config)

            if not self.gestion_bd.ouvrir_base_de_donnees():
                QMessageBox.critical(self, "Erreur",
                    "Impossible d'ouvrir la base de données\n\n"
                    "Vérifiez que :\n"
                    "• MySQL Server est démarré\n"
                    "• Les paramètres de connexion sont corrects\n"
                    "• La base de données existe")
                sys.exit(1)

            if not self.gestion_bd.creer_tables():
                QMessageBox.critical(self, "Erreur", "Impossible de créer les tables")
                sys.exit(1)

            # Récupérer la connexion à la base de données
            self.db = self.gestion_bd

            print("Base de données initialisée avec succès")

        except Exception as e:
            QMessageBox.critical(self, "Erreur d'initialisation",
                f"Erreur lors de l'initialisation :\n{str(e)}")
            sys.exit(1)

    def ajouter_equipement(self):
        """Méthode pour ajouter un équipement - À personnaliser avec votre propre dialog"""
        # TODO: Créer votre propre QDialog personnalisé ici
        # Exemple de structure :
        # dialog = VotreDialogPersonnalise(self)
        # if dialog.exec() == QDialog.Accepted:
        #     # Traiter les données du dialog
        #     pass
        print("Bouton ajouter équipement cliqué - À implémenter avec votre dialog personnalisé")

    def actualiser_tableau_equipements(self):
        """Met à jour le tableau des équipements"""
        try:
            # TODO: Cette méthode devra être adaptée selon votre nouvelle classe GestionEquipements
            # Pour l'instant, on initialise juste un tableau vide
            self.ui.tableWidget_equipement.setRowCount(0)
            self.ui.tableWidget_equipement.setColumnCount(7)
            headers = ["ID", "Type", "Marque", "Modèle", "Numéro de série", "État", "Utilisateur"]
            self.ui.tableWidget_equipement.setHorizontalHeaderLabels(headers)

            # Ajuster la largeur des colonnes
            self.ui.tableWidget_equipement.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la mise à jour du tableau :\n{str(e)}")

    def closeEvent(self, event):
        """Gestionnaire de fermeture de l'application"""
        if hasattr(self, 'gestion_bd'):
            self.gestion_bd.fermer_base_de_donnees()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = fen_main()
    widget.show()
    sys.exit(app.exec())
