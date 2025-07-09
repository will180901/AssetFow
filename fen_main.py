# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase

from ui_form import Ui_fen_main
from NavigationManager import NavigationManager
from GestionBD import GestionBD
from GestionUtilisateur import GestionUtilisateur
from DialogEnregUtilisateur import DialogEnregUtilisateur

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
            "password": "motdepasse", # Changez ceci
            "db_name": "test",
            "replace": False
        }

        self.init_database()

        self.gestion_utilisateurs = GestionUtilisateur(self.db)

        # --- Connecter les boutons ---
        self.ui.btn_ajouter_equipement.clicked.connect(self.ajouter_equipement)
        self.ui.btn_ajouter_utilisateur.clicked.connect(self.ouvrir_dialog_ajout_utilisateur)

        self.actualiser_tableau_equipements()
        self.actualiser_tableau_utilisateurs()

    def init_database(self):
        """Initialise la connexion à la base de données"""
        try:
            self.gestion_bd = GestionBD(**self.db_config)
            if not self.gestion_bd.ouvrir_base_de_donnees():
                QMessageBox.critical(self, "Erreur", "Impossible d'ouvrir la base de données...")
                sys.exit(1)
            if not self.gestion_bd.creer_tables():
                QMessageBox.critical(self, "Erreur", "Impossible de créer les tables")
                sys.exit(1)
            self.db = self.gestion_bd
            print("Base de données initialisée avec succès")
        except Exception as e:
            QMessageBox.critical(self, "Erreur d'initialisation", f"Erreur lors de l'initialisation :\n{str(e)}")
            sys.exit(1)

    def ouvrir_dialog_ajout_utilisateur(self):
        """
        Affiche la fenêtre de dialogue avec un calque semi-transparent en arrière-plan.
        """
        # --- Création du calque (overlay) ---
        self.overlay = QWidget(self.ui.centralwidget)
        # Style du calque : noir avec 60% d'opacité (150 sur 255)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        self.overlay.setGeometry(self.ui.centralwidget.rect())
        self.overlay.show()
        # On s'assure qu'il est bien au-dessus des autres widgets de la page
        self.overlay.raise_()

        # On crée une instance de notre dialogue
        dialog = DialogEnregUtilisateur(self.gestion_utilisateurs, self)

        # On utilise un bloc try...finally pour s'assurer que le calque est TOUJOURS caché,
        # même si le dialogue est fermé avec la croix.
        try:
            if dialog.exec():
                print("Dialogue fermé avec succès, mise à jour du tableau.")
                self.actualiser_tableau_utilisateurs()
        finally:
            # On cache le calque une fois le dialogue fermé
            self.overlay.hide()
            # On le supprime pour libérer la mémoire
            self.overlay.deleteLater()

    def ajouter_equipement(self):
        print("Bouton ajouter équipement cliqué - À implémenter.")

    def actualiser_tableau_equipements(self):
        try:
            self.ui.tableWidget_equipement.setRowCount(0)
            self.ui.tableWidget_equipement.setColumnCount(7)
            headers = ["ID", "Type", "Marque", "Modèle", "N° série", "État", "Utilisateur"]
            self.ui.tableWidget_equipement.setHorizontalHeaderLabels(headers)
            self.ui.tableWidget_equipement.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur MàJ tableau équipements :\n{str(e)}")

    def creer_badge_role(self, role):
        """Crée un badge stylisé pour le rôle de l'utilisateur"""
        badge = QLabel(role)
        badge.setAlignment(Qt.AlignCenter)
        badge.setMinimumHeight(30)
        badge.setMaximumHeight(30)

        # Styles basés sur le rôle
        styles = {
            "Admin": """
                background-color: rgba(220, 53, 69, 0.15);
                color: #dc3545;
                border: 1px solid rgba(220, 53, 69, 0.3);
                border-radius: 12px;
                padding: 4px 12px;
                font-weight: 500;
            """,
            "Superviseur": """
                background-color: rgba(0, 123, 255, 0.15);
                color: #0069d9;
                border: 1px solid rgba(0, 123, 255, 0.3);
                border-radius: 12px;
                padding: 4px 12px;
                font-weight: 500;
            """,
            "Technicien": """
                background-color: rgba(40, 167, 69, 0.15);
                color: #28a745;
                border: 1px solid rgba(40, 167, 69, 0.3);
                border-radius: 12px;
                padding: 4px 12px;
                font-weight: 500;
            """,
            "Utilisateur": """
                background-color: rgba(108, 117, 125, 0.15);
                color: #6c757d;
                border: 1px solid rgba(108, 117, 125, 0.3);
                border-radius: 12px;
                padding: 4px 12px;
                font-weight: 500;
            """
        }

        # Appliquer le style approprié ou un style par défaut
        badge.setStyleSheet(styles.get(role, """
            background-color: rgba(255, 193, 7, 0.15);
            color: #ffc107;
            border: 1px solid rgba(255, 193, 7, 0.3);
            border-radius: 12px;
            padding: 4px 12px;
            font-weight: 500;
        """))

        return badge

    def actualiser_tableau_utilisateurs(self):
        """Met à jour le QTableWidget avec la liste des utilisateurs de la BDD."""
        try:
            utilisateurs = self.gestion_utilisateurs.lister_utilisateurs()
            table = self.ui.tableWidget_utilisateur

            table.setRowCount(0)
            table.setColumnCount(4)
            headers = ["ID", "Nom complet", "Email", "Rôle"]
            table.setHorizontalHeaderLabels(headers)

            for row_num, user in enumerate(utilisateurs):
                table.insertRow(row_num)
                table.setItem(row_num, 0, QTableWidgetItem(str(user['id'])))
                table.setItem(row_num, 1, QTableWidgetItem(user['nom']))
                table.setItem(row_num, 2, QTableWidgetItem(user['email']))

                # Créer et ajouter le badge pour le rôle
                badge = self.creer_badge_role(user['role'])
                table.setCellWidget(row_num, 3, badge)

                # Ajuster la hauteur de la ligne pour le badge
                table.setRowHeight(row_num, 40)

            table.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur MàJ tableau utilisateurs :\n{str(e)}")

    def closeEvent(self, event):
        if hasattr(self, 'gestion_bd'):
            self.gestion_bd.fermer_base_de_donnees()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = fen_main()
    widget.show()
    sys.exit(app.exec())
