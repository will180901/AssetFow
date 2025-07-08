# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fen_enreg_utilisateur.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import rc_icones

class Ui_fen_enreg_utilisateur(object):
    def setupUi(self, fen_enreg_utilisateur):
        if not fen_enreg_utilisateur.objectName():
            fen_enreg_utilisateur.setObjectName(u"fen_enreg_utilisateur")
        fen_enreg_utilisateur.resize(383, 383)
        fen_enreg_utilisateur.setMinimumSize(QSize(383, 383))
        fen_enreg_utilisateur.setStyleSheet(u"\n"
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
"QDialog , #fen_enreg_utilisateur{\n"
"\n"
"		\n"
"			border-radius :10px ;\n"
"\n"
"}\n"
"\n"
"QGroupBox{\n"
"\n"
"		border:none ;\n"
"\n"
"}\n"
"\n"
"#label_affiche_erreur_validation{\n"
"		\n"
"		\n"
"	font: italic 8pt \"Segoe UI\";\n"
"\n"
"	\n"
"	color: rgb(218, 17, 54);\n"
"\n"
"}\n"
"\n"
"#label_description_fenetre{\n"
"\n"
"	\n"
"	font: 300 8pt \"Bahnschrift\";\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"\n"
"}\n"
"\n"
"#label_titre_fenetre{\n"
"	\n"
"		\n"
"	font: 600 12pt \"Bahnschrift\";\n"
"\n"
"}\n"
"\n"
"\n"
"#fen_enreg_utilisateur{\n"
"\n"
"		background-color: rgb(255, 255, 255);\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(229, 234, 239);\n"
"}\n"
"\n"
"\n"
"/*===============================================\n"
"   BOUTONS STANDARDS\n"
"   ===============================================*/\n"
"\n"
"\n"
"QPushButton {\n"
"    bac"
                        "kground-color: rgb(13, 110, 253);\n"
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
"QToolButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"#btn_annuler_ajout_utilisateur{\n"
"\n"
"		border:none ;\n"
"	   color: rgb(64, 64, 64);\n"
"		background : transparent ;\n"
"\n"
"}\n"
"\n"
"#btn_annuler_ajout_utilisateur:hover{\n"
"\n"
"	color:rgb(13, 110, 253);\n"
"\n"
"}\n"
"\n"
"/*===============================================\n"
"   \u00c9L\u00c9MENTS DE FORMULAIRE\n"
"   ===============================================*/\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 6"
                        "px;\n"
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
"    padding: 6px 24px 6px 8px;\n"
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
""
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
"QComboBox::down-arrow:pressed {\n"
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
"QComboBox"
                        " QAbstractItemView::item {\n"
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
"   ===============================================*/\n"
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
" "
                        "   background-color: rgb(248, 249, 250);\n"
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
"QDoubleSpinBox::up-button:pressed, QSpinBox::up-button:pressed {\n"
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
""
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
"    image: url(:/icon_gris/chevron-down.svg);\n"
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
"QDoubleSpinBox::down-arrow:disabled, QSpinBox::down-arrow:disa"
                        "bled {\n"
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
"    border: 1px solid #0d6efd;\n"
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
"    "
                        "background-color: rgba(229, 234, 239, 0.6);\n"
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
"    background-color: rgb(248, 249, 250);\n"
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
"    margin-right:"
                        " 2px;\n"
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
"    background-color: rgb(233, 236, 239);\n"
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
"    heig"
                        "ht: 12px;\n"
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
"    border-radius: 4px;\n"
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
"QScrollBar:"
                        ":add-line:vertical,\n"
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
"   S\u00c9PARATEURS\n"
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
"/*================"
                        "===============================\n"
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
"    color: #333333;\n"
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
"    border-botto"
                        "m: 1px solid #e0e0e0;\n"
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
"/*===============================================\n"
"BADGES DE MONTANT - STYLE INSPIR\u00c9 DES BADGES DE STATUT MODERNES\n"
"===============================================*/\n"
"\n"
"QLabel.MontantBadgePositif {\n"
"    background-color: rgba(34, 197, 94, 0.2);\n"
"    color: #22c55e;\n"
"    border: 1px solid rgba(34, 197, 94, 0.3);\n"
"    border-radius: 8px;\n"
"    padding: 3px 6px;\n"
"    min-width: 55px;\n"
"    max-width: 105px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 6pt;\n"
"}\n"
"\n"
"QLabel.MontantBadgeNegatif {\n"
"    background-color: rgba(239, 68, 68, 0.2);\n"
"    color: #ef4444;\n"
"    border: 1px solid rgba(239, 68, 68, 0.3);\n"
"    border-radius: 8px;\n"
"    pad"
                        "ding: 3px 6px;\n"
"    min-width: 55px;\n"
"    max-width: 105px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 6pt;\n"
"}\n"
"\n"
"QLabel.MontantBadgeNeutre {\n"
"    background-color: rgba(107, 114, 128, 0.2);\n"
"    color: #6b7280;\n"
"    border: 1px solid rgba(107, 114, 128, 0.3);\n"
"    border-radius: 8px;\n"
"    padding: 3px 6px;\n"
"    min-width: 55px;\n"
"    max-width: 105px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 6pt;\n"
"}\n"
"\n"
"QLabel.MontantBadgePending {\n"
"    background-color: rgba(245, 158, 11, 0.2);\n"
"    color: #f59e0b;\n"
"    border: 1px solid rgba(245, 158, 11, 0.3);\n"
"    border-radius: 8px;\n"
"    padding: 3px 6px;\n"
"    min-width: 55px;\n"
"    max-width: 105px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 6pt;\n"
"}\n"
"\n"
"QLabel.MontantBadgeCritique {\n"
"    background-color: rgba(239, 68, 68, 0.9);\n"
"    color: white;\n"
"    border: 1px solid #ef4444;\n"
"    border-radius:"
                        " 12px;\n"
"    padding: 4px 12px;\n"
"    min-width: 60px;\n"
"    max-width: 120px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/*===============================================\n"
"VARIANTES AVEC EFFET HOVER (OPTIONNEL)\n"
"===============================================*/\n"
"\n"
"QLabel.MontantBadgePositif:hover {\n"
"    background-color: rgba(34, 197, 94, 0.3);\n"
"    border: 1px solid rgba(34, 197, 94, 0.5);\n"
"}\n"
"\n"
"QLabel.MontantBadgeNegatif:hover {\n"
"    background-color: rgba(239, 68, 68, 0.3);\n"
"    border: 1px solid rgba(239, 68, 68, 0.5);\n"
"}\n"
"\n"
"QLabel.MontantBadgeNeutre:hover {\n"
"    background-color: rgba(107, 114, 128, 0.3);\n"
"    border: 1px solid rgba(107, 114, 128, 0.5);\n"
"}\n"
"\n"
"QLabel.MontantBadgePending:hover {\n"
"    background-color: rgba(245, 158, 11, 0.3);\n"
"    border: 1px solid rgba(245, 158, 11, 0.5);\n"
"}\n"
"\n"
"\n"
"/* Style pour les boutons actifs */\n"
"#BarreLaterale QToolButton[active=\"true"
                        "\"] {\n"
"    background-color: #1a3c6c;\n"
"    color: white;\n"
"    padding: 4px 4px;\n"
"    text-align: left;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Style pour les boutons normaux */\n"
"#BarreLaterale QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgb(73, 80, 87);\n"
"    padding: 4px 4px;\n"
"    text-align: left;\n"
"    border-radius: 4px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(fen_enreg_utilisateur)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.widget = QWidget(fen_enreg_utilisateur)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_titre_fenetre = QLabel(self.widget)
        self.label_titre_fenetre.setObjectName(u"label_titre_fenetre")

        self.verticalLayout.addWidget(self.label_titre_fenetre)

        self.label_description_fenetre = QLabel(self.widget)
        self.label_description_fenetre.setObjectName(u"label_description_fenetre")

        self.verticalLayout.addWidget(self.label_description_fenetre)


        self.verticalLayout_6.addWidget(self.widget)

        self.line = QFrame(fen_enreg_utilisateur)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.groupBox = QGroupBox(fen_enreg_utilisateur)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 15, 2, 2)
        self.lineEdit_nom_complet_utilisateur = QLineEdit(self.groupBox)
        self.lineEdit_nom_complet_utilisateur.setObjectName(u"lineEdit_nom_complet_utilisateur")

        self.verticalLayout_2.addWidget(self.lineEdit_nom_complet_utilisateur)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(fen_enreg_utilisateur)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 15, 2, 2)
        self.lineEdit_email_utilisateur = QLineEdit(self.groupBox_2)
        self.lineEdit_email_utilisateur.setObjectName(u"lineEdit_email_utilisateur")

        self.verticalLayout_3.addWidget(self.lineEdit_email_utilisateur)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(fen_enreg_utilisateur)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 15, 2, 2)
        self.lineEdit_mot_de_passe = QLineEdit(self.groupBox_4)
        self.lineEdit_mot_de_passe.setObjectName(u"lineEdit_mot_de_passe")
        self.lineEdit_mot_de_passe.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout_7.addWidget(self.lineEdit_mot_de_passe)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(fen_enreg_utilisateur)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 15, 2, 2)
        self.lineEdit_confirmation_mot_de_passe = QLineEdit(self.groupBox_5)
        self.lineEdit_confirmation_mot_de_passe.setObjectName(u"lineEdit_confirmation_mot_de_passe")
        self.lineEdit_confirmation_mot_de_passe.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_8.addWidget(self.lineEdit_confirmation_mot_de_passe)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(fen_enreg_utilisateur)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 15, 2, 2)
        self.comboBox_role_utilisateur = QComboBox(self.groupBox_3)
        self.comboBox_role_utilisateur.setObjectName(u"comboBox_role_utilisateur")

        self.verticalLayout_4.addWidget(self.comboBox_role_utilisateur)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.label_affiche_erreur_validation = QLabel(fen_enreg_utilisateur)
        self.label_affiche_erreur_validation.setObjectName(u"label_affiche_erreur_validation")
        self.label_affiche_erreur_validation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_affiche_erreur_validation, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_3 = QWidget(fen_enreg_utilisateur)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.btn_annuler_ajout_utilisateur = QPushButton(self.widget_2)
        self.btn_annuler_ajout_utilisateur.setObjectName(u"btn_annuler_ajout_utilisateur")
        self.btn_annuler_ajout_utilisateur.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_annuler_ajout_utilisateur)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon_blanc/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.widget_3)


        self.retranslateUi(fen_enreg_utilisateur)

        QMetaObject.connectSlotsByName(fen_enreg_utilisateur)
    # setupUi

    def retranslateUi(self, fen_enreg_utilisateur):
        fen_enreg_utilisateur.setWindowTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"Dialog", None))
        self.label_titre_fenetre.setText(QCoreApplication.translate("fen_enreg_utilisateur", u"Ajouter un Utilisateur", None))
        self.label_description_fenetre.setText(QCoreApplication.translate("fen_enreg_utilisateur", u"Cr\u00e9er un nouveau compte utilisateur et assign\u00e9 un r\u00f4le", None))
        self.groupBox.setTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"Nom complet", None))
        self.lineEdit_nom_complet_utilisateur.setInputMask("")
        self.lineEdit_nom_complet_utilisateur.setPlaceholderText(QCoreApplication.translate("fen_enreg_utilisateur", u"EX : Samba denos", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"Email", None))
        self.lineEdit_email_utilisateur.setPlaceholderText(QCoreApplication.translate("fen_enreg_utilisateur", u"Xyz@gmail.com", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"Mot de passe ", None))
        self.lineEdit_mot_de_passe.setPlaceholderText(QCoreApplication.translate("fen_enreg_utilisateur", u"Cr\u00e9er votre mot de passe ", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"Confirmation de mot de passe ", None))
        self.lineEdit_confirmation_mot_de_passe.setPlaceholderText(QCoreApplication.translate("fen_enreg_utilisateur", u"Confirmer votre mot de passe ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("fen_enreg_utilisateur", u"R\u00f4le ", None))
        self.label_affiche_erreur_validation.setText("")
        self.btn_annuler_ajout_utilisateur.setText(QCoreApplication.translate("fen_enreg_utilisateur", u"Annuler", None))
        self.pushButton.setText(QCoreApplication.translate("fen_enreg_utilisateur", u"Cr\u00e9er", None))
    # retranslateUi

