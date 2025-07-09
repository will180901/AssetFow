# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QTableWidgetItem, QWidget, QHeaderView, QToolButton, QMenu, QWidgetAction, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from functools import partial

from ui_form import Ui_fen_main
from NavigationManager import NavigationManager
from GestionBD import GestionBD
from GestionUtilisateur import GestionUtilisateur
from GestionBadge import GestionBadge
from DialogEnregUtilisateur import DialogEnregUtilisateur
from FenModifierUtilisateur import FenModifierUtilisateur


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
            "db_name": "AssetFlow",
            "replace": False
        }

        # Initialisation des composants
        self.init_navigation()
        self.init_database()
        self.init_gestionnaires()
        self.connecter_signaux()
        self.actualiser_tableaux()

        # Appliquer un effet glassmorphism (miroir/transparent) au tableau utilisateur avec header semi-transparent
        self.ui.tableWidget_utilisateur.setStyleSheet('''
            QTableWidget {
                background: rgba(255, 255, 255, 0.30);
                border-radius: 8px;
                border: 1px solid rgba(200,200,200,0.18);
                backdrop-filter: blur(8px);
                -qt-background-role: 10;
                font-size: 10pt;
            }
            QHeaderView::section {
                background: rgba(25, 118, 210, 0.18);
                color: #1976D2;
                border: none;
                font-weight: 600;
                font-size: 10pt;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                padding: 6px 0px;
            }
            QTableWidget::item {
                background: transparent;
                font-size: 10pt;
            }
        ''')

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
            table.setColumnCount(5)
            headers = ["ID", "Nom complet", "Email", "Rôle", "Action"]
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

                # Ajout du bouton d'action
                btn_action = QToolButton()
                # Utilisation d'une icône locale ou fallback unicode
                icone = QIcon(":/icon_blanc/more-horizontal.svg") if QIcon.hasThemeIcon(":/icon_blanc/more-horizontal.svg") else QIcon()
                btn_action.setIcon(icone)
                if icone.isNull():
                    btn_action.setText("⋮")  # fallback unicode
                btn_action.setPopupMode(QToolButton.InstantPopup)
                btn_action.setStyleSheet("""
                    QToolButton {
                        border: none;
                        background: transparent;
                        padding: 0px 8px;
                        min-width: 32px;
                        min-height: 28px;
                        font-size: 10pt;
                    }
                    QToolButton:hover {
                        background: rgba(25, 118, 210, 0.10);
                        border-radius: 14px;
                    }
                """)
                # --- Menu flottant moderne ---
                # --- Menu flottant responsive (actions horizontales sur large, verticales sur petit) ---
                class ResponsiveMenu(QMenu):
                    def __init__(self, parent=None):
                        super().__init__(parent)
                        self.setStyleSheet("""
                            QMenu {
                                background: #fff;
                                border-radius: 14px;
                                border: 1px solid #e0e0e0;
                                padding: 8px 0px;
                                min-width: 160px;
                                font: 10pt 'Segoe UI';
                                box-shadow: 0px 8px 24px rgba(0,0,0,0.08);
                                clip-path: inset(0 round 14px);
                            }
                        """)
                        self.widget = QWidget(self)
                        self.layout_h = QHBoxLayout()
                        self.layout_h.setContentsMargins(8, 8, 8, 8)
                        self.layout_h.setSpacing(12)
                        self.btn_modifier = QPushButton("Modifier")
                        self.btn_supprimer = QPushButton("Supprimer")
                        self.btn_modifier.setCursor(Qt.PointingHandCursor)
                        self.btn_supprimer.setCursor(Qt.PointingHandCursor)
                        self.btn_supprimer.setStyleSheet("color: #d32f2f; font-weight: bold;")
                        self.btn_modifier.setStyleSheet("color: #1976D2; font-weight: 500;")
                        self.btn_modifier.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                        self.btn_supprimer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                        self.layout_h.addWidget(self.btn_modifier)
                        self.layout_h.addWidget(self.btn_supprimer)
                        self.widget.setLayout(self.layout_h)
                        action_widget = QWidgetAction(self)
                        action_widget.setDefaultWidget(self.widget)
                        self.addAction(action_widget)
                        # Responsive : vertical si largeur < 320px
                        self.widget.resizeEvent = self._resize_event
                    def _resize_event(self, event):
                        if self.widget.width() < 320:
                            layout = QVBoxLayout()
                            layout.setContentsMargins(8, 8, 8, 8)
                            layout.setSpacing(8)
                            layout.addWidget(self.btn_modifier)
                            layout.addWidget(self.btn_supprimer)
                            self.widget.setLayout(layout)
                        else:
                            self.widget.setLayout(self.layout_h)
                        QWidget.resizeEvent(self.widget, event)

                # --- OUTIL ROBUSTE POUR TROUVER LA LIGNE DU BOUTON ---
                def get_row_for_button(btn, table):
                    for r in range(table.rowCount()):
                        if table.cellWidget(r, 4) is btn:
                            return r
                    return -1

                def supprimer_utilisateur_depuis_bouton(btn, table=table, utilisateurs=utilisateurs):
                    row = get_row_for_button(btn, table)
                    if row < 0:
                        return
                    id_item = table.item(row, 0)
                    if not id_item:
                        return
                    id_utilisateur = id_item.text()
                    utilisateur = next((u for u in utilisateurs if str(u['id']) == id_utilisateur), None)
                    if utilisateur is None:
                        return
                    rep = QMessageBox.question(self, "Confirmation", f"Supprimer l'utilisateur {utilisateur['nom']} ?", QMessageBox.Yes | QMessageBox.No)
                    if rep == QMessageBox.Yes:
                        if self.gestion_utilisateurs.supprimer_utilisateur(utilisateur['id']):
                            self.actualiser_tableau_utilisateurs()
                        else:
                            QMessageBox.critical(self, "Erreur", "La suppression a échoué.")

                def ouvrir_dialog_modification_depuis_bouton(btn, table=table, utilisateurs=utilisateurs):
                    row = get_row_for_button(btn, table)
                    if row < 0:
                        return
                    id_item = table.item(row, 0)
                    if not id_item:
                        return
                    id_utilisateur = id_item.text()
                    utilisateur = next((u for u in utilisateurs if str(u['id']) == id_utilisateur), None)
                    if utilisateur is None:
                        return
                    dialog = FenModifierUtilisateur(utilisateur, self.gestion_utilisateurs, self)
                    if dialog.exec():
                        self.actualiser_tableau_utilisateurs()

                # --- Connexion des actions ---
                menu = ResponsiveMenu()
                # Connexion des actions
                menu.btn_modifier.clicked.connect(partial(ouvrir_dialog_modification_depuis_bouton, btn_action))
                menu.btn_supprimer.clicked.connect(partial(supprimer_utilisateur_depuis_bouton, btn_action))

                # Nettoyage préalable de la cellule Action pour éviter les doublons ou widgets fantômes
                if table.cellWidget(row_num, 4) is not None:
                    old_widget = table.cellWidget(row_num, 4)
                    old_widget.deleteLater()
                    table.removeCellWidget(row_num, 4)
                table.setCellWidget(row_num, 4, btn_action)
                table.setRowHeight(row_num, 40)

                # Affichage du menu flottant sous le bouton action au clic
                def make_show_menu(btn, menu):
                    def show_menu(_=None):
                        rect = btn.rect()
                        global_pos = btn.mapToGlobal(rect.bottomLeft())
                        menu_width = menu.sizeHint().width()
                        btn_width = btn.width()
                        global_pos.setX(global_pos.x() + (btn_width // 2) - (menu_width // 2))
                        menu.popup(global_pos)
                    return show_menu
                btn_action.clicked.disconnect()
                btn_action.clicked.connect(make_show_menu(btn_action, menu))

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
    widget.showMaximized()
    sys.exit(app.exec())
