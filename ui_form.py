# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
import rc_icones

class Ui_fen_main(object):
    def setupUi(self, fen_main):
        if not fen_main.objectName():
            fen_main.setObjectName(u"fen_main")
        fen_main.resize(801, 600)
        fen_main.setStyleSheet(u"\n"
"*{\n"
"\n"
"		/*border: 1px solid rgb(133, 133, 133);*/\n"
"		\n"
"		color: rgb(74, 74, 74);\n"
"		font: 350 10pt \"Bahnschrift\";\n"
"\n"
"}\n"
"\n"
"\n"
"#zone_haut_fixe_btn_ajout_tickets{\n"
"\n"
"	background-color: rgb(240, 245, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"#carte_equipement,#carte_tickets,#carte_equipement_3,#carte_graphe_chart,#carte_graphe_chart_2,#carte_alertes_recentes{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(229, 234, 239);\n"
"\n"
"}\n"
"\n"
"#label_titre_alerte_recentes{\n"
"\n"
"font: 700 16pt \"Bahnschrift\";\n"
"\n"
"}\n"
"\n"
"#label_nombre_equipements,#label_nombre_tickets_ouvert,#label_nombre_intervention_encours{\n"
"		\n"
"		\n"
"	font: 700 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"#label_titre_etat_equipement,#label_titre_etat_equipement_2{\n"
"\n"
"\n"
"	font: 700 12pt \"Bahnschrift\";\n"
"\n"
"}\n"
"\n"
"\n"
"#label_sous_titre_etat_equipement,#label_sous_titre_etat_equipement_2,#label_sous_titre_alertes_recentes{\n"
"\n"
""
                        "font: 300 10pt \"Segoe UI\";\n"
"	color: rgb(47, 47, 47);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"#label_description_carte,#label_description_carte_2,#label_description_carte_3{\n"
"\n"
"		\n"
"	\n"
"	font: 300 10pt \"Segoe UI\";\n"
"	color: rgb(47, 47, 47);\n"
"\n"
"}\n"
"\n"
"#label_equipement_totaux,#label_equipement_totaux_2,#label_equipement_totaux_3{\n"
"\n"
"font: 700 12pt \"Bahnschrift\";\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#label_titre_page_ETU{\n"
"\n"
"		\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"\n"
"}\n"
"\n"
"\n"
"#label_nom_utilisateur_connecte{\n"
"\n"
"		\n"
"	font: 350 9pt \"Segoe UI\";\n"
"\n"
"\n"
"}\n"
"#label_nom_utilisateur_connecte{\n"
"\n"
"			\n"
"	font: 600 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"#label_role_utilisateur{\n"
"		\n"
"		\n"
"	font: 350 9pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"\n"
"#label_photo_profil  {\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgb(111, 66, 193);\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    background-color: rgba(111, 66, 193, "
                        "0.1);\n"
"}\n"
"\n"
"#label_photo_profil:hover {\n"
"    background-color: rgba(111, 66, 193, 0.2);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*===============================================\n"
"   BOUTONS DE LA BARRE LAT\u00c9RALE\n"
"   ===============================================*/\n"
"\n"
"#BarreLaterale {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-right: 1px solid rgb(229, 234, 239);\n"
"	\n"
"	\n"
"}\n"
"\n"
"#BarreLaterale QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgb(73, 80, 87);\n"
"    padding: 4px 4px;\n"
"    text-align: left;\n"
"    border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"#BarreLaterale QToolButton:hover {\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"#BarreLaterale QToolButton:pressed {\n"
"    background-color: rgba(229, 234, 239, 150);\n"
"    color: rgb(13, 110, 253);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#BarreLaterale QToolButton:focus {\n"
"    outline: 2px solid #0d6efd !important;\n"
"    outline-offset: -1px !importa"
                        "nt;\n"
"    background-color: #e9ecef !important;\n"
"}\n"
"\n"
"#btn_icon_return_tableau_de_bord{\n"
"\n"
"\n"
"		font: 600 12pt \"Bahnschrift\";\n"
"	\n"
"	\n"
"	color: rgb(95, 95, 95);\n"
"\n"
"	background : none ;\n"
"	border-radius:none ;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#btn_icon_return_tableau_de_bord:hover{\n"
"\n"
"\n"
"		\n"
"	color: rgb(13, 110, 253);\n"
"\n"
"	\n"
"\n"
"}\n"
"\n"
"\n"
"#centralwidget,#page_ETU,#page_equipement,#page_tickets,#page_utilisateurs,\n"
"#page_tableau_de_bord,#page_utilisateurs,\n"
"#scrollAreaWidgetContents,#scrollArea{\n"
"\n"
"		\n"
"	background-color: rgb(240, 245, 255);\n"
"		\n"
"	border:none ;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*===============================================\n"
"   BARRE DE NAVIGATION ET RECHERCHE\n"
"   ===============================================*/\n"
"\n"
"#bar_nav {\n"
"    border-bottom: 1px solid rgb(229, 234, 239);\n"
"	 background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"#indicat_recherche {\n"
"    background: transparent;\n"
"    "
                        "border: none;\n"
"    padding: 0;\n"
"}\n"
"\n"
"#ZoneRecherche {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#BarreRecherche {\n"
"    border: 1px solid rgba(206, 212, 218, 180);\n"
"    border-radius: 4px;\n"
"	 background-color: rgba(240, 244, 248, 200);\n"
"    padding: 6px;\n"
"}\n"
"\n"
"#BarreRecherche:hover {\n"
"    border-bottom: 1px solid rgb(13, 110, 253);\n"
"   	\n"
"	background-color: rgb(240, 245, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*===============================================\n"
"   BOUTONS STANDARDS\n"
"   ===============================================*/\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(13, 110, 253);\n"
"    padding: 6px 12px;\n"
"    border-radius: 4px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: 500;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(10, 88, 202);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(8, 77, 178);\n"
"}\n"
"\n"
"QToolBut"
                        "ton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/*===============================================\n"
"   \u00c9L\u00c9MENTS DE FORMULAIRE\n"
"   ===============================================*/\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    color: #495057;\n"
"}\n"
"\n"
"QLineEdit:hover, QTextEdit:hover {\n"
"    border: 1px solid #0d6efd;\n"
"    background-color: rgb(248, 249, 250);\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, \n"
"QComboBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid #0d6efd;\n"
"    outline: none;\n"
"}\n"
"\n"
"/*===============================================\n"
"   COMBOBOX\n"
"   ===============================================*/\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 6px 24px 6px 8"
                        "px;\n"
"    color: #495057;\n"
"    font-size: 13px;\n"
"    min-height: 18px;\n"
"    selection-background-color: #0d6efd;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #0d6efd;\n"
"    background-color: rgb(248, 249, 250);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #0d6efd;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: rgb(240, 244, 248);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: rgba(229, 234, 239, 0.3);\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"    background-color: rgba(229, 234, 239, 0.5);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon_gris/chevron-down.svg);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QCo"
                        "mboBox::down-arrow:pressed {\n"
"    image: url(:/icon_noir/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #0d6efd;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: #0d6efd;\n"
"    selection-color: white;\n"
"    padding: 2px;\n"
"    outline: none;\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 28px;\n"
"    padding: 0 8px;\n"
"    border-bottom: 1px solid rgba(229, 234, 239, 0.5);\n"
"    color: #495057;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:last {\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(13, 110, 253, 0.1);\n"
"    color: #0d6efd;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #0d6efd;\n"
"    color: white;\n"
"}\n"
"\n"
"/*===============================================\n"
"   SPINBOX ET DOUBLESPINBOX\n"
"   ==============="
                        "================================*/\n"
"\n"
"QDoubleSpinBox, QSpinBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 6px 8px;\n"
"    color: #495057;\n"
"    font-size: 13px;\n"
"    min-height: 18px;\n"
"    selection-background-color: #0d6efd;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover, QSpinBox:hover {\n"
"    border-color: #0d6efd;\n"
"    background-color: rgb(248, 249, 250);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus, QSpinBox:focus {\n"
"    border: 1px solid #0d6efd;\n"
"    outline: none;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button, QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"    height: 10px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover, QSpinBox::up-button:hover {\n"
"    background-color: rgba(229, 234, 239, 0.3);\n"
"}\n"
"\n"
"QDoubleSpinBox::up"
                        "-button:pressed, QSpinBox::up-button:pressed {\n"
"    background-color: rgba(229, 234, 239, 0.5);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button, QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"    height: 10px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: rgba(229, 234, 239, 0.3);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: rgba(229, 234, 239, 0.5);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {\n"
"    image: url(:/icon_gris/chevron-up.svg);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow:hover, QSpinBox::up-arrow:hover {\n"
"    image: url(:/icon_noir/chevron-up.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {\n"
"    image:"
                        " url(:/icon_gris/chevron-down.svg);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow:hover, QSpinBox::down-arrow:hover {\n"
"    image: url(:/icon_noir/chevron-down.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow:disabled, QSpinBox::up-arrow:disabled {\n"
"    image: url(:/icon_gris/chevron-up-disabled.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow:disabled, QSpinBox::down-arrow:disabled {\n"
"    image: url(:/icon_gris/chevron-down-disabled.svg);\n"
"}\n"
"\n"
"/*===============================================\n"
"   DATEEDIT\n"
"   ===============================================*/\n"
"\n"
"QDateEdit {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 6px 24px 6px 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #495057;\n"
"    font-size: 13px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border-color: #0d6efd;\n"
"    background-color: rgb(248, 249, 250);\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 1px"
                        " solid #0d6efd;\n"
"    outline: none;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border: none;\n"
"    border-left: 1px solid #ced4da;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    background-color: rgba(229, 234, 239, 0.3);\n"
"}\n"
"\n"
"QDateEdit::drop-down:hover {\n"
"    background-color: rgba(229, 234, 239, 0.6);\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/icon_gris/calendar.svg);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/*===============================================\n"
"   ONGLETS DE TRANSACTION\n"
"   ===============================================*/\n"
"\n"
"#mes_onglets_page_transaction {\n"
"    background-color: rgb(248, 249, 250);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#mes_onglets_page_transaction::pane {\n"
"    border: none;\n"
"    border-radius: 0 0 4px 4px;\n"
"    background-color: rgb(248,"
                        " 249, 250);\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar {\n"
"    background: transparent;\n"
"    border: none;\n"
"    spacing: 4px;\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar::tab {\n"
"    background-color: rgba(229, 234, 239, 0.5);\n"
"    border: 1px solid rgb(229, 234, 239);\n"
"    border-bottom: none;\n"
"    border-radius: 4px 4px 0 0;\n"
"    padding: 8px 16px;\n"
"    margin-right: 2px;\n"
"    min-width: 100px;\n"
"    color: rgb(108, 117, 125);\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar::tab:selected {\n"
"    background-color: rgb(248, 249, 250);\n"
"    border-color: rgb(229, 234, 239);\n"
"    color: rgb(73, 80, 87);\n"
"    font-weight: 600;\n"
"    border-bottom: 2px solid #0d6efd;\n"
"    margin-bottom: -1px;\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar::tab:hover {\n"
"    background-color: rgba(229, 234, 239, 0.8);\n"
"    color: rgb(13, 110, 253);\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar::tab:selected:hover {\n"
"    background-c"
                        "olor: rgb(233, 236, 239);\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar QToolButton {\n"
"    background: rgb(229, 234, 239);\n"
"    border-radius: 3px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"#mes_onglets_page_transaction > QTabBar QToolButton::right-arrow,\n"
"#mes_onglets_page_transaction > QTabBar QToolButton::left-arrow {\n"
"    image: url(:/icon_gris/chevron-right.svg);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/*===============================================\n"
"   BARRES DE D\u00c9FILEMENT\n"
"   ===============================================*/\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgba(248, 249, 250, 0);\n"
"    width: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgba(248, 249, 250, 0);\n"
"    height: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgba(206, 212, 218, 0.5);\n"
"    border"
                        "-radius: 4px;\n"
"    min-height: 20px;\n"
"    min-width: 20px;\n"
"    opacity: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgba(13, 110, 253, 0.6);\n"
"    opacity: 1;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed,\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgba(8, 77, 178, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0;\n"
"    width: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover,\n"
"QScrollBar:horizontal:hover {\n"
"    background-color: rgba(248, 249, 250, 0.3);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/*===============================================\n"
"   S\u00c9PA"
                        "RATEURS\n"
"   ===============================================*/\n"
"\n"
"Line {\n"
"    background-color: rgb(229, 234, 239);\n"
"    border-radius: 1px;\n"
"    border: 1px solid rgb(229, 234, 239);\n"
"    width: 1px;\n"
"}\n"
"\n"
"#line, #line_2 ,#line_3{\n"
"    border: none;\n"
"    background-color: rgba(206, 212, 218, 0.7);\n"
"    border-radius: 1px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/*===============================================\n"
"   TABLEAUX - STYLE AM\u00c9LIOR\u00c9 AVEC CELLULES PLUS GRANDES\n"
"   ===============================================*/\n"
"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #ffffff;\n"
"    gridline-color: #e0e0e0;\n"
"    color: #333333;\n"
"    border:  1px solid  rgb(224, 224, 224);\n"
"    selection-background-color: #e3f2fd;\n"
"    selection-color: #1976d2;\n"
"    outline: none;\n"
"	border-radius : 8px ;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #f5f5f5;\n"
"    color: #333333;"
                        "\n"
"    padding: 6px 4px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"    text-align: left;\n"
"    min-height: 35px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::vertical::section {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    min-width: 45px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px 4px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"    border-right: none;\n"
"    min-height: 40px;\n"
"    font-size: 7pt;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #e3f2fd;\n"
"    color: #1976d2;\n"
"}\n"
"\n"
"\n"
"/*===============================================\n"
"               BADGES DE R\u00d4LE - STYLE MODERNE\n"
"               ===============================================*/\n"
"            .RoleBadgeAdmin {\n"
"                background-color: rgba(220, 53, 69, 0.15);\n"
"                color: #dc3545"
                        ";\n"
"                border: 1px solid rgba(220, 53, 69, 0.3);\n"
"                border-radius: 12px;\n"
"                padding: 4px 12px;\n"
"                font-weight: 500;\n"
"            }\n"
"            \n"
"            .RoleBadgeSuperviseur {\n"
"                background-color: rgba(0, 123, 255, 0.15);\n"
"                color: #0069d9;\n"
"                border: 1px solid rgba(0, 123, 255, 0.3);\n"
"                border-radius: 12px;\n"
"                padding: 4px 12px;\n"
"                font-weight: 500;\n"
"            }\n"
"            \n"
"            .RoleBadgeTechnicien {\n"
"                background-color: rgba(40, 167, 69, 0.15);\n"
"                color: #28a745;\n"
"                border: 1px solid rgba(40, 167, 69, 0.3);\n"
"                border-radius: 12px;\n"
"                padding: 4px 12px;\n"
"                font-weight: 500;\n"
"            }\n"
"            \n"
"            .RoleBadgeUtilisateur {\n"
"                background-color: rgba(108, 117, 125, 0.1"
                        "5);\n"
"                color: #6c757d;\n"
"                border: 1px solid rgba(108, 117, 125, 0.3);\n"
"                border-radius: 12px;\n"
"                padding: 4px 12px;\n"
"                font-weight: 500;\n"
"            }\n"
"            \n"
"            .RoleBadgeDefault {\n"
"                background-color: rgba(255, 193, 7, 0.15);\n"
"                color: #ffc107;\n"
"                border: 1px solid rgba(255, 193, 7, 0.3);\n"
"                border-radius: 12px;\n"
"                padding: 4px 12px;\n"
"                font-weight: 500;\n"
"            }\n"
"\n"
"\n"
"/* Style pour les boutons actifs */\n"
"#BarreLaterale QToolButton[active=\"true\"] {\n"
"   background-color: rgb(13, 110, 253);\n"
"    padding: 6px 12px;\n"
"    border-radius: 4px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: 500;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Style pour les boutons normaux */\n"
"#BarreLaterale QToolButton {\n"
"    background-color: transparent;\n"
""
                        "    border: none;\n"
"    color: rgb(73, 80, 87);\n"
"    padding: 4px 4px;\n"
"    text-align: left;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QWidget(fen_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BarreLaterale = QWidget(self.centralwidget)
        self.BarreLaterale.setObjectName(u"BarreLaterale")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarreLaterale.sizePolicy().hasHeightForWidth())
        self.BarreLaterale.setSizePolicy(sizePolicy)
        self.BarreLaterale.setMinimumSize(QSize(170, 581))
        self.verticalLayout = QVBoxLayout(self.BarreLaterale)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.btn_icon_return_tableau_de_bord = QPushButton(self.BarreLaterale)
        self.btn_icon_return_tableau_de_bord.setObjectName(u"btn_icon_return_tableau_de_bord")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_icon_return_tableau_de_bord.sizePolicy().hasHeightForWidth())
        self.btn_icon_return_tableau_de_bord.setSizePolicy(sizePolicy1)
        self.btn_icon_return_tableau_de_bord.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon_noir/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_icon_return_tableau_de_bord.setIcon(icon)
        self.btn_icon_return_tableau_de_bord.setIconSize(QSize(15, 15))

        self.verticalLayout.addWidget(self.btn_icon_return_tableau_de_bord)

        self.line = QFrame(self.BarreLaterale)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(100, 0))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_4 = QWidget(self.BarreLaterale)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.btn_bar_nav_tableau_de_bord = QToolButton(self.widget_4)
        self.btn_bar_nav_tableau_de_bord.setObjectName(u"btn_bar_nav_tableau_de_bord")
        sizePolicy1.setHeightForWidth(self.btn_bar_nav_tableau_de_bord.sizePolicy().hasHeightForWidth())
        self.btn_bar_nav_tableau_de_bord.setSizePolicy(sizePolicy1)
        self.btn_bar_nav_tableau_de_bord.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon_gris/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_bar_nav_tableau_de_bord.setIcon(icon1)
        self.btn_bar_nav_tableau_de_bord.setIconSize(QSize(15, 15))
        self.btn_bar_nav_tableau_de_bord.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btn_bar_nav_tableau_de_bord)

        self.btn_bar_nav_equipement = QToolButton(self.widget_4)
        self.btn_bar_nav_equipement.setObjectName(u"btn_bar_nav_equipement")
        sizePolicy1.setHeightForWidth(self.btn_bar_nav_equipement.sizePolicy().hasHeightForWidth())
        self.btn_bar_nav_equipement.setSizePolicy(sizePolicy1)
        self.btn_bar_nav_equipement.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon_gris/monitor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_bar_nav_equipement.setIcon(icon2)
        self.btn_bar_nav_equipement.setIconSize(QSize(15, 15))
        self.btn_bar_nav_equipement.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btn_bar_nav_equipement)

        self.btn_bar_nav_tickets = QToolButton(self.widget_4)
        self.btn_bar_nav_tickets.setObjectName(u"btn_bar_nav_tickets")
        sizePolicy1.setHeightForWidth(self.btn_bar_nav_tickets.sizePolicy().hasHeightForWidth())
        self.btn_bar_nav_tickets.setSizePolicy(sizePolicy1)
        self.btn_bar_nav_tickets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon_gris/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_bar_nav_tickets.setIcon(icon3)
        self.btn_bar_nav_tickets.setIconSize(QSize(15, 15))
        self.btn_bar_nav_tickets.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btn_bar_nav_tickets)

        self.btn_bar_nav_utilisateurs = QToolButton(self.widget_4)
        self.btn_bar_nav_utilisateurs.setObjectName(u"btn_bar_nav_utilisateurs")
        sizePolicy1.setHeightForWidth(self.btn_bar_nav_utilisateurs.sizePolicy().hasHeightForWidth())
        self.btn_bar_nav_utilisateurs.setSizePolicy(sizePolicy1)
        self.btn_bar_nav_utilisateurs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icon_gris/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_bar_nav_utilisateurs.setIcon(icon4)
        self.btn_bar_nav_utilisateurs.setIconSize(QSize(15, 15))
        self.btn_bar_nav_utilisateurs.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btn_bar_nav_utilisateurs)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.BarreLaterale)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_photo_profil = QLabel(self.widget_5)
        self.label_photo_profil.setObjectName(u"label_photo_profil")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_photo_profil.sizePolicy().hasHeightForWidth())
        self.label_photo_profil.setSizePolicy(sizePolicy3)
        self.label_photo_profil.setMinimumSize(QSize(31, 31))

        self.horizontalLayout_2.addWidget(self.label_photo_profil)

        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label_nom_utilisateur_connecte = QLabel(self.widget)
        self.label_nom_utilisateur_connecte.setObjectName(u"label_nom_utilisateur_connecte")

        self.verticalLayout_3.addWidget(self.label_nom_utilisateur_connecte)

        self.label_role_utilisateur = QLabel(self.widget)
        self.label_role_utilisateur.setObjectName(u"label_role_utilisateur")

        self.verticalLayout_3.addWidget(self.label_role_utilisateur)


        self.horizontalLayout_2.addWidget(self.widget)

        self.toolButton = QToolButton(self.widget_5)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icon_gris/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon5)
        self.toolButton.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.BarreLaterale)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(631, 581))
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bar_nav = QWidget(self.widget_2)
        self.bar_nav.setObjectName(u"bar_nav")
        sizePolicy1.setHeightForWidth(self.bar_nav.sizePolicy().hasHeightForWidth())
        self.bar_nav.setSizePolicy(sizePolicy1)
        self.bar_nav.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.bar_nav)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.BarreRecherche = QWidget(self.bar_nav)
        self.BarreRecherche.setObjectName(u"BarreRecherche")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.BarreRecherche.sizePolicy().hasHeightForWidth())
        self.BarreRecherche.setSizePolicy(sizePolicy4)
        self.BarreRecherche.setMinimumSize(QSize(251, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.BarreRecherche)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.ZoneRecherche = QLineEdit(self.BarreRecherche)
        self.ZoneRecherche.setObjectName(u"ZoneRecherche")

        self.horizontalLayout_3.addWidget(self.ZoneRecherche)

        self.indicat_recherche = QToolButton(self.BarreRecherche)
        self.indicat_recherche.setObjectName(u"indicat_recherche")
        icon6 = QIcon()
        icon6.addFile(u":/icon_gris/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.indicat_recherche.setIcon(icon6)
        self.indicat_recherche.setIconSize(QSize(15, 15))

        self.horizontalLayout_3.addWidget(self.indicat_recherche, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_4.addWidget(self.BarreRecherche, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.btn_notification_bar_nav = QToolButton(self.bar_nav)
        self.btn_notification_bar_nav.setObjectName(u"btn_notification_bar_nav")
        sizePolicy4.setHeightForWidth(self.btn_notification_bar_nav.sizePolicy().hasHeightForWidth())
        self.btn_notification_bar_nav.setSizePolicy(sizePolicy4)
        self.btn_notification_bar_nav.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icon_gris/bell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_notification_bar_nav.setIcon(icon7)
        self.btn_notification_bar_nav.setIconSize(QSize(15, 15))

        self.horizontalLayout_4.addWidget(self.btn_notification_bar_nav, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.bar_nav)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_tableau_de_bord = QWidget()
        self.page_tableau_de_bord.setObjectName(u"page_tableau_de_bord")
        self.verticalLayout_6 = QVBoxLayout(self.page_tableau_de_bord)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.scrollArea = QScrollArea(self.page_tableau_de_bord)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 900, 900))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(900, 900))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.label_titre_tableauDeBord = QLabel(self.widget_3)
        self.label_titre_tableauDeBord.setObjectName(u"label_titre_tableauDeBord")
        self.label_titre_tableauDeBord.setGeometry(QRect(20, 10, 111, 16))

        self.verticalLayout_16.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(561, 141))
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 2, 2, 2)
        self.carte_equipement = QWidget(self.widget_6)
        self.carte_equipement.setObjectName(u"carte_equipement")
        self.carte_equipement.setMinimumSize(QSize(241, 121))
        self.verticalLayout_7 = QVBoxLayout(self.carte_equipement)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.widget_8 = QWidget(self.carte_equipement)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_equipement_totaux = QLabel(self.widget_8)
        self.label_equipement_totaux.setObjectName(u"label_equipement_totaux")

        self.horizontalLayout_6.addWidget(self.label_equipement_totaux, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 20))
        self.label.setStyleSheet(u"border-image: url(:/icon_bleu/monitor.svg);")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_7.addWidget(self.widget_8)

        self.label_nombre_equipements = QLabel(self.carte_equipement)
        self.label_nombre_equipements.setObjectName(u"label_nombre_equipements")
        self.label_nombre_equipements.setMinimumSize(QSize(50, 0))
        self.label_nombre_equipements.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_nombre_equipements, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_description_carte = QLabel(self.carte_equipement)
        self.label_description_carte.setObjectName(u"label_description_carte")

        self.verticalLayout_7.addWidget(self.label_description_carte)


        self.gridLayout.addWidget(self.carte_equipement, 0, 0, 1, 1)

        self.carte_tickets = QWidget(self.widget_6)
        self.carte_tickets.setObjectName(u"carte_tickets")
        self.carte_tickets.setMinimumSize(QSize(241, 121))
        self.verticalLayout_8 = QVBoxLayout(self.carte_tickets)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.widget_9 = QWidget(self.carte_tickets)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_titre_tickets = QLabel(self.widget_9)
        self.label_titre_tickets.setObjectName(u"label_titre_tickets")

        self.horizontalLayout_7.addWidget(self.label_titre_tickets, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setStyleSheet(u"border-image: url(:/icon_orange_warning/layers.svg);")

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_8.addWidget(self.widget_9)

        self.label_nombre_tickets_ouvert = QLabel(self.carte_tickets)
        self.label_nombre_tickets_ouvert.setObjectName(u"label_nombre_tickets_ouvert")
        self.label_nombre_tickets_ouvert.setMinimumSize(QSize(50, 0))
        self.label_nombre_tickets_ouvert.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_nombre_tickets_ouvert, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_description_carte_tickets = QLabel(self.carte_tickets)
        self.label_description_carte_tickets.setObjectName(u"label_description_carte_tickets")

        self.verticalLayout_8.addWidget(self.label_description_carte_tickets)


        self.gridLayout.addWidget(self.carte_tickets, 0, 1, 1, 1)

        self.carte_equipement_3 = QWidget(self.widget_6)
        self.carte_equipement_3.setObjectName(u"carte_equipement_3")
        self.carte_equipement_3.setMinimumSize(QSize(241, 121))
        self.verticalLayout_9 = QVBoxLayout(self.carte_equipement_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_10 = QWidget(self.carte_equipement_3)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_equipement_totaux_3 = QLabel(self.widget_10)
        self.label_equipement_totaux_3.setObjectName(u"label_equipement_totaux_3")

        self.horizontalLayout_8.addWidget(self.label_equipement_totaux_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setStyleSheet(u"border-image: url(:/icon_vert_succes/tool.svg);")

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.label_nombre_intervention_encours = QLabel(self.carte_equipement_3)
        self.label_nombre_intervention_encours.setObjectName(u"label_nombre_intervention_encours")
        self.label_nombre_intervention_encours.setMinimumSize(QSize(50, 0))
        self.label_nombre_intervention_encours.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_nombre_intervention_encours, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_description_carte_3 = QLabel(self.carte_equipement_3)
        self.label_description_carte_3.setObjectName(u"label_description_carte_3")

        self.verticalLayout_9.addWidget(self.label_description_carte_3)


        self.gridLayout.addWidget(self.carte_equipement_3, 0, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(881, 361))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.carte_graphe_chart = QWidget(self.widget_7)
        self.carte_graphe_chart.setObjectName(u"carte_graphe_chart")
        self.carte_graphe_chart.setMinimumSize(QSize(401, 291))
        self.verticalLayout_10 = QVBoxLayout(self.carte_graphe_chart)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_11 = QWidget(self.carte_graphe_chart)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy2.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy2)
        self.widget_11.setMinimumSize(QSize(381, 20))
        self.verticalLayout_11 = QVBoxLayout(self.widget_11)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, -1, 2)
        self.label_titre_etat_equipement = QLabel(self.widget_11)
        self.label_titre_etat_equipement.setObjectName(u"label_titre_etat_equipement")

        self.verticalLayout_11.addWidget(self.label_titre_etat_equipement)

        self.label_sous_titre_etat_equipement = QLabel(self.widget_11)
        self.label_sous_titre_etat_equipement.setObjectName(u"label_sous_titre_etat_equipement")

        self.verticalLayout_11.addWidget(self.label_sous_titre_etat_equipement)


        self.verticalLayout_10.addWidget(self.widget_11, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.line_3 = QFrame(self.carte_graphe_chart)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_3)

        self.espace_graphes_equipements_en_reparation = QWidget(self.carte_graphe_chart)
        self.espace_graphes_equipements_en_reparation.setObjectName(u"espace_graphes_equipements_en_reparation")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.espace_graphes_equipements_en_reparation.sizePolicy().hasHeightForWidth())
        self.espace_graphes_equipements_en_reparation.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.espace_graphes_equipements_en_reparation)


        self.gridLayout_2.addWidget(self.carte_graphe_chart, 0, 0, 1, 1)

        self.carte_graphe_chart_2 = QWidget(self.widget_7)
        self.carte_graphe_chart_2.setObjectName(u"carte_graphe_chart_2")
        self.carte_graphe_chart_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.carte_graphe_chart_2)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.widget_13 = QWidget(self.carte_graphe_chart_2)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.widget_13.setMinimumSize(QSize(0, 20))
        self.verticalLayout_13 = QVBoxLayout(self.widget_13)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(8, 8, 8, 8)
        self.label_titre_etat_equipement_2 = QLabel(self.widget_13)
        self.label_titre_etat_equipement_2.setObjectName(u"label_titre_etat_equipement_2")

        self.verticalLayout_13.addWidget(self.label_titre_etat_equipement_2)

        self.label_sous_titre_etat_equipement_2 = QLabel(self.widget_13)
        self.label_sous_titre_etat_equipement_2.setObjectName(u"label_sous_titre_etat_equipement_2")

        self.verticalLayout_13.addWidget(self.label_sous_titre_etat_equipement_2)


        self.verticalLayout_12.addWidget(self.widget_13, 0, Qt.AlignmentFlag.AlignLeft)

        self.line_2 = QFrame(self.carte_graphe_chart_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.espace_graphes_noumbre_tickets_ouvert = QWidget(self.carte_graphe_chart_2)
        self.espace_graphes_noumbre_tickets_ouvert.setObjectName(u"espace_graphes_noumbre_tickets_ouvert")
        sizePolicy5.setHeightForWidth(self.espace_graphes_noumbre_tickets_ouvert.sizePolicy().hasHeightForWidth())
        self.espace_graphes_noumbre_tickets_ouvert.setSizePolicy(sizePolicy5)

        self.verticalLayout_12.addWidget(self.espace_graphes_noumbre_tickets_ouvert)


        self.gridLayout_2.addWidget(self.carte_graphe_chart_2, 0, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_7)

        self.carte_alertes_recentes = QWidget(self.scrollAreaWidgetContents)
        self.carte_alertes_recentes.setObjectName(u"carte_alertes_recentes")
        self.carte_alertes_recentes.setMinimumSize(QSize(881, 301))
        self.verticalLayout_15 = QVBoxLayout(self.carte_alertes_recentes)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_15 = QWidget(self.carte_alertes_recentes)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.verticalLayout_14 = QVBoxLayout(self.widget_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_titre_alerte_recentes = QLabel(self.widget_15)
        self.label_titre_alerte_recentes.setObjectName(u"label_titre_alerte_recentes")

        self.verticalLayout_14.addWidget(self.label_titre_alerte_recentes)

        self.label_sous_titre_alertes_recentes = QLabel(self.widget_15)
        self.label_sous_titre_alertes_recentes.setObjectName(u"label_sous_titre_alertes_recentes")

        self.verticalLayout_14.addWidget(self.label_sous_titre_alertes_recentes)


        self.verticalLayout_15.addWidget(self.widget_15, 0, Qt.AlignmentFlag.AlignLeft)

        self.tableWidget = QTableWidget(self.carte_alertes_recentes)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_15.addWidget(self.tableWidget)


        self.verticalLayout_16.addWidget(self.carte_alertes_recentes)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_tableau_de_bord)
        self.page_equipement = QWidget()
        self.page_equipement.setObjectName(u"page_equipement")
        self.verticalLayout_5 = QVBoxLayout(self.page_equipement)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.zone_haut_fixe_btn_ajout_equipement = QWidget(self.page_equipement)
        self.zone_haut_fixe_btn_ajout_equipement.setObjectName(u"zone_haut_fixe_btn_ajout_equipement")
        sizePolicy1.setHeightForWidth(self.zone_haut_fixe_btn_ajout_equipement.sizePolicy().hasHeightForWidth())
        self.zone_haut_fixe_btn_ajout_equipement.setSizePolicy(sizePolicy1)
        self.zone_haut_fixe_btn_ajout_equipement.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_5 = QHBoxLayout(self.zone_haut_fixe_btn_ajout_equipement)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_titre_page_equipement = QLabel(self.zone_haut_fixe_btn_ajout_equipement)
        self.label_titre_page_equipement.setObjectName(u"label_titre_page_equipement")
        sizePolicy.setHeightForWidth(self.label_titre_page_equipement.sizePolicy().hasHeightForWidth())
        self.label_titre_page_equipement.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_titre_page_equipement, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_ajouter_equipement = QPushButton(self.zone_haut_fixe_btn_ajout_equipement)
        self.btn_ajouter_equipement.setObjectName(u"btn_ajouter_equipement")
        sizePolicy3.setHeightForWidth(self.btn_ajouter_equipement.sizePolicy().hasHeightForWidth())
        self.btn_ajouter_equipement.setSizePolicy(sizePolicy3)
        self.btn_ajouter_equipement.setMinimumSize(QSize(151, 30))
        self.btn_ajouter_equipement.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icon_blanc/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ajouter_equipement.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.btn_ajouter_equipement, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.zone_haut_fixe_btn_ajout_equipement)

        self.widget_12 = QWidget(self.page_equipement)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.tableWidget_equipement = QTableWidget(self.widget_12)
        self.tableWidget_equipement.setObjectName(u"tableWidget_equipement")
        self.tableWidget_equipement.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_equipement.setShowGrid(False)
        self.tableWidget_equipement.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_equipement.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget_equipement.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_equipement.verticalHeader().setVisible(False)
        self.tableWidget_equipement.verticalHeader().setProperty(u"showSortIndicator", True)

        self.horizontalLayout_11.addWidget(self.tableWidget_equipement)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.page_equipement)
        self.page_tickets = QWidget()
        self.page_tickets.setObjectName(u"page_tickets")
        self.verticalLayout_17 = QVBoxLayout(self.page_tickets)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.zone_haut_fixe_btn_ajout_tickets = QWidget(self.page_tickets)
        self.zone_haut_fixe_btn_ajout_tickets.setObjectName(u"zone_haut_fixe_btn_ajout_tickets")
        sizePolicy1.setHeightForWidth(self.zone_haut_fixe_btn_ajout_tickets.sizePolicy().hasHeightForWidth())
        self.zone_haut_fixe_btn_ajout_tickets.setSizePolicy(sizePolicy1)
        self.zone_haut_fixe_btn_ajout_tickets.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_9 = QHBoxLayout(self.zone_haut_fixe_btn_ajout_tickets)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.label_titre_page_tickets = QLabel(self.zone_haut_fixe_btn_ajout_tickets)
        self.label_titre_page_tickets.setObjectName(u"label_titre_page_tickets")
        sizePolicy.setHeightForWidth(self.label_titre_page_tickets.sizePolicy().hasHeightForWidth())
        self.label_titre_page_tickets.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_titre_page_tickets, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_ajouter_tickets = QPushButton(self.zone_haut_fixe_btn_ajout_tickets)
        self.btn_ajouter_tickets.setObjectName(u"btn_ajouter_tickets")
        sizePolicy3.setHeightForWidth(self.btn_ajouter_tickets.sizePolicy().hasHeightForWidth())
        self.btn_ajouter_tickets.setSizePolicy(sizePolicy3)
        self.btn_ajouter_tickets.setMinimumSize(QSize(151, 30))
        self.btn_ajouter_tickets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ajouter_tickets.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.btn_ajouter_tickets, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_17.addWidget(self.zone_haut_fixe_btn_ajout_tickets)

        self.widget_14 = QWidget(self.page_tickets)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.tableWidget_tickets = QTableWidget(self.widget_14)
        self.tableWidget_tickets.setObjectName(u"tableWidget_tickets")
        self.tableWidget_tickets.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_tickets.setShowGrid(False)
        self.tableWidget_tickets.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_tickets.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget_tickets.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tickets.verticalHeader().setVisible(False)
        self.tableWidget_tickets.verticalHeader().setProperty(u"showSortIndicator", True)

        self.horizontalLayout_12.addWidget(self.tableWidget_tickets)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_17.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.page_tickets)
        self.page_utilisateurs = QWidget()
        self.page_utilisateurs.setObjectName(u"page_utilisateurs")
        self.verticalLayout_18 = QVBoxLayout(self.page_utilisateurs)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.zone_haut_fixe_btn_ajout_utilisateur = QWidget(self.page_utilisateurs)
        self.zone_haut_fixe_btn_ajout_utilisateur.setObjectName(u"zone_haut_fixe_btn_ajout_utilisateur")
        sizePolicy1.setHeightForWidth(self.zone_haut_fixe_btn_ajout_utilisateur.sizePolicy().hasHeightForWidth())
        self.zone_haut_fixe_btn_ajout_utilisateur.setSizePolicy(sizePolicy1)
        self.zone_haut_fixe_btn_ajout_utilisateur.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.zone_haut_fixe_btn_ajout_utilisateur)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_titre_page_tickets_2 = QLabel(self.zone_haut_fixe_btn_ajout_utilisateur)
        self.label_titre_page_tickets_2.setObjectName(u"label_titre_page_tickets_2")
        sizePolicy.setHeightForWidth(self.label_titre_page_tickets_2.sizePolicy().hasHeightForWidth())
        self.label_titre_page_tickets_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_titre_page_tickets_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_ajouter_utilisateur = QPushButton(self.zone_haut_fixe_btn_ajout_utilisateur)
        self.btn_ajouter_utilisateur.setObjectName(u"btn_ajouter_utilisateur")
        sizePolicy3.setHeightForWidth(self.btn_ajouter_utilisateur.sizePolicy().hasHeightForWidth())
        self.btn_ajouter_utilisateur.setSizePolicy(sizePolicy3)
        self.btn_ajouter_utilisateur.setMinimumSize(QSize(151, 30))
        self.btn_ajouter_utilisateur.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ajouter_utilisateur.setIcon(icon8)

        self.horizontalLayout_10.addWidget(self.btn_ajouter_utilisateur, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_18.addWidget(self.zone_haut_fixe_btn_ajout_utilisateur)

        self.widget_16 = QWidget(self.page_utilisateurs)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.tableWidget_utilisateur = QTableWidget(self.widget_16)
        self.tableWidget_utilisateur.setObjectName(u"tableWidget_utilisateur")
        self.tableWidget_utilisateur.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_utilisateur.setShowGrid(False)
        self.tableWidget_utilisateur.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_utilisateur.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget_utilisateur.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_utilisateur.verticalHeader().setVisible(False)
        self.tableWidget_utilisateur.verticalHeader().setProperty(u"showSortIndicator", True)

        self.horizontalLayout_13.addWidget(self.tableWidget_utilisateur)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_18.addWidget(self.widget_16)

        self.stackedWidget.addWidget(self.page_utilisateurs)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        fen_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(fen_main)

        QMetaObject.connectSlotsByName(fen_main)
    # setupUi

    def retranslateUi(self, fen_main):
        fen_main.setWindowTitle(QCoreApplication.translate("fen_main", u"fen_main", None))
        self.btn_icon_return_tableau_de_bord.setText(QCoreApplication.translate("fen_main", u"AssetFlow Manager", None))
        self.btn_bar_nav_tableau_de_bord.setText(QCoreApplication.translate("fen_main", u"Tableau de bord ", None))
        self.btn_bar_nav_equipement.setText(QCoreApplication.translate("fen_main", u"Equipements ", None))
        self.btn_bar_nav_tickets.setText(QCoreApplication.translate("fen_main", u"Tickets", None))
        self.btn_bar_nav_utilisateurs.setText(QCoreApplication.translate("fen_main", u"utlisateurs ", None))
        self.label_photo_profil.setText("")
        self.label_nom_utilisateur_connecte.setText(QCoreApplication.translate("fen_main", u"TextLabel", None))
        self.label_role_utilisateur.setText(QCoreApplication.translate("fen_main", u"TextLabel", None))
        self.toolButton.setText("")
        self.ZoneRecherche.setPlaceholderText(QCoreApplication.translate("fen_main", u"Rechercher dans la page ...", None))
        self.indicat_recherche.setText("")
        self.btn_notification_bar_nav.setText("")
        self.label_titre_tableauDeBord.setText(QCoreApplication.translate("fen_main", u"Tableau de bord", None))
        self.label_equipement_totaux.setText(QCoreApplication.translate("fen_main", u"Equipements Totaux", None))
        self.label.setText("")
        self.label_nombre_equipements.setText(QCoreApplication.translate("fen_main", u"7", None))
        self.label_description_carte.setText(QCoreApplication.translate("fen_main", u"Total des Equipements dans le parc ", None))
        self.label_titre_tickets.setText(QCoreApplication.translate("fen_main", u"Tickets ouvert", None))
        self.label_2.setText("")
        self.label_nombre_tickets_ouvert.setText(QCoreApplication.translate("fen_main", u"7", None))
        self.label_description_carte_tickets.setText(QCoreApplication.translate("fen_main", u"Tickets non r\u00e9solus", None))
        self.label_equipement_totaux_3.setText(QCoreApplication.translate("fen_main", u"Intervention en cours", None))
        self.label_3.setText("")
        self.label_nombre_intervention_encours.setText(QCoreApplication.translate("fen_main", u"4", None))
        self.label_description_carte_3.setText(QCoreApplication.translate("fen_main", u"Tickets actuellement trait\u00e9s", None))
        self.label_titre_etat_equipement.setText(QCoreApplication.translate("fen_main", u"Etats des Equipements", None))
        self.label_sous_titre_etat_equipement.setText(QCoreApplication.translate("fen_main", u"R\u00e9paration des \u00e9quipement  par statut", None))
        self.label_titre_etat_equipement_2.setText(QCoreApplication.translate("fen_main", u"Tickets par priorite", None))
        self.label_sous_titre_etat_equipement_2.setText(QCoreApplication.translate("fen_main", u"Nombre de tickets ouvert  par niveau de priorit\u00e9", None))
        self.label_titre_alerte_recentes.setText(QCoreApplication.translate("fen_main", u"Alertes R\u00e9centes", None))
        self.label_sous_titre_alertes_recentes.setText(QCoreApplication.translate("fen_main", u"Notifications importantes concernant  le parc informatique", None))
        self.label_titre_page_equipement.setText(QCoreApplication.translate("fen_main", u"Gestions des \u00e9quipement ", None))
        self.btn_ajouter_equipement.setText(QCoreApplication.translate("fen_main", u"Ajouter un Equipement ", None))
        self.label_titre_page_tickets.setText(QCoreApplication.translate("fen_main", u"Gestions des tickets", None))
        self.btn_ajouter_tickets.setText(QCoreApplication.translate("fen_main", u"Ajouter un Ticket", None))
        self.label_titre_page_tickets_2.setText(QCoreApplication.translate("fen_main", u"Gestion des utilisateurs", None))
        self.btn_ajouter_utilisateur.setText(QCoreApplication.translate("fen_main", u"Ajouter un Utilisateur", None))
    # retranslateUi

