# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QTableWidgetItem, QWidget, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase

from ui_form import Ui_fen_main
from NavigationManager import NavigationManager
from GestionBD import GestionBD
from GestionUtilisateur import GestionUtilisateur
from GestionBadge import GestionBadge
from DialogEnregUtilisateur import DialogEnregUtilisateur


class fen_main(QMainWindow):
    """
    Fenêtre principale de l'application de gestion d'équipements et d'utilisateurs.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fen_main()
        self.ui.setupUi(self)

        # Configuration de la base de données
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "motdepasse",  # TODO: Sécuriser le mot de passe
            "db_name": "test",
            "replace": False
        }

        # Initialisation des composants
        self.init_navigation()
        self.init_database()
        self.init_gestionnaires()
        self.connecter_signaux()
        self.actualiser_tableaux()

    def init_navigation(self):
        """Initialise le gestionnaire de navigation."""
        self.navigation_manager = NavigationManager(self.ui)
        self.navigation_manager.show_page(self.ui.page_tableau_de_bord)

    def init_database(self):
        """Initialise la connexion à la base de données."""
        try:
            self.gestion_bd = GestionBD(**self.db_config)

            if not self.gestion_bd.ouvrir_base_de_donnees():
                self._afficher_erreur_critique("Impossible d'ouvrir la base de données")
                return False

            if not self.gestion_bd.creer_tables():
                self._afficher_erreur_critique("Impossible de créer les tables")
                return False

            self.db = self.gestion_bd
            print("Base de données initialisée avec succès")
            return True

        except Exception as e:
            self._afficher_erreur_critique(f"Erreur lors de l'initialisation :\n{str(e)}")
            return False

    def init_gestionnaires(self):
        """Initialise les gestionnaires de données."""
        if hasattr(self, 'db'):
            self.gestion_utilisateurs = GestionUtilisateur(self.db)
        else:
            print("Erreur: Base de données non initialisée")

    def connecter_signaux(self):
        """Connecte les signaux des boutons aux méthodes appropriées."""
        self.ui.btn_ajouter_equipement.clicked.connect(self.ajouter_equipement)
        self.ui.btn_ajouter_utilisateur.clicked.connect(self.ouvrir_dialog_ajout_utilisateur)

    def actualiser_tableaux(self):
        """Met à jour tous les tableaux de l'interface."""
        self.actualiser_tableau_equipements()
        self.actualiser_tableau_utilisateurs()

    def _afficher_erreur_critique(self, message):
        """Affiche une erreur critique et ferme l'application."""
        QMessageBox.critical(self, "Erreur", message)
        sys.exit(1)

    def ouvrir_dialog_ajout_utilisateur(self):
        """
        Affiche la fenêtre de dialogue d'ajout d'utilisateur avec un calque semi-transparent.
        """
        # Création du calque overlay
        overlay = self._creer_overlay()

        try:
            # Création et affichage du dialogue
            dialog = DialogEnregUtilisateur(self.gestion_utilisateurs, self)

            if dialog.exec():
                print("Dialogue fermé avec succès, mise à jour du tableau.")
                self.actualiser_tableau_utilisateurs()

        finally:
            # Nettoyage du calque
            self._nettoyer_overlay(overlay)

    def _creer_overlay(self):
        """Crée un calque semi-transparent pour les dialogues."""
        overlay = QWidget(self.ui.centralwidget)
        overlay.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        overlay.setGeometry(self.ui.centralwidget.rect())
        overlay.show()
        overlay.raise_()
        return overlay

    def _nettoyer_overlay(self, overlay):
        """Nettoie le calque overlay."""
        if overlay:
            overlay.hide()
            overlay.deleteLater()

    def ajouter_equipement(self):
        """Méthode pour ajouter un équipement - À implémenter."""
        print("Bouton ajouter équipement cliqué - À implémenter.")
        # TODO: Implémenter l'ajout d'équipement

    def actualiser_tableau_equipements(self):
        """Met à jour le tableau des équipements."""
        try:
            table = self.ui.tableWidget_equipement

            # Configuration du tableau
            table.setRowCount(0)
            table.setColumnCount(7)
            headers = ["ID", "Type", "Marque", "Modèle", "N° série", "État", "Utilisateur"]
            table.setHorizontalHeaderLabels(headers)

            # Configuration des colonnes
            self._configurer_colonnes_tableau(table)

        except Exception as e:
            self._afficher_erreur(f"Erreur MàJ tableau équipements :\n{str(e)}")

    def actualiser_tableau_utilisateurs(self):
        """Met à jour le tableau des utilisateurs."""
        try:
            if not hasattr(self, 'gestion_utilisateurs'):
                print("Gestionnaire d'utilisateurs non initialisé")
                return

            utilisateurs = self.gestion_utilisateurs.lister_utilisateurs()
            table = self.ui.tableWidget_utilisateur

            # Configuration du tableau
            table.setRowCount(0)
            table.setColumnCount(4)
            headers = ["ID", "Nom complet", "Email", "Rôle"]
            table.setHorizontalHeaderLabels(headers)

            # Configuration des colonnes
            self._configurer_colonnes_tableau(table)

            # Ajout des données
            for row_num, user in enumerate(utilisateurs):
                table.insertRow(row_num)
                table.setItem(row_num, 0, QTableWidgetItem(str(user['id'])))
                table.setItem(row_num, 1, QTableWidgetItem(user['nom']))
                table.setItem(row_num, 2, QTableWidgetItem(user['email']))

                # Ajout du badge pour le rôle
                badge = self._creer_badge_role(user['role'])
                table.setCellWidget(row_num, 3, badge)

                # Ajustement de la hauteur de ligne
                table.setRowHeight(row_num, 40)

        except Exception as e:
            self._afficher_erreur(f"Erreur MàJ tableau utilisateurs :\n{str(e)}")

    def _configurer_colonnes_tableau(self, table):
        """Configure les colonnes d'un tableau pour qu'elles aient une largeur égale."""
        header = table.horizontalHeader()
        for i in range(table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    def _creer_badge_role(self, role):
        """Crée un badge stylisé pour le rôle de l'utilisateur."""
        return GestionBadge.creer_badge_role(role)

    def _afficher_erreur(self, message):
        """Affiche un message d'erreur non critique."""
        QMessageBox.critical(self, "Erreur", message)

    def closeEvent(self, event):
        """Gestionnaire d'événement de fermeture de la fenêtre."""
        if hasattr(self, 'gestion_bd'):
            self.gestion_bd.fermer_base_de_donnees()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = fen_main()
    widget.show()
    sys.exit(app.exec())
