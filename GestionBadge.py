from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class GestionBadge:
    @staticmethod
    def creer_badge_role(role):
        """Crée un badge stylisé et coloré selon le rôle de l'utilisateur."""
        badge = QLabel(role)
        badge.setAlignment(Qt.AlignCenter)
        badge.setMinimumHeight(28)
        badge.setMaximumHeight(26)
        badge.setFixedWidth(135)  # Largeur fixe à 135px
        badge.setMargin(0)
        badge.setContentsMargins(0, 0, 0, 0)

        # Normalisation du rôle pour la correspondance
        role_normalise = role.strip().lower()
        if role_normalise in ["administrateur", "admin"]:
            color = "#1976D2"
            border = "1px solid #1976D2"
            bg = "rgba(25, 118, 210, 0.10)"
            text_color = "#1976D2"
        elif role_normalise == "technicien":
            color = "#43A047"
            border = "1px solid #43A047"
            bg = "rgba(67, 160, 71, 0.10)"
            text_color = "#43A047"
        else:
            color = "transparent"
            border = "1px solid #B0B0B0"
            bg = "transparent"
            text_color = "#888"
        
        badge.setStyleSheet(f"""
            QLabel {{
                background: {bg};
                color: {text_color};
                border-radius: 8px;
                border: {border};
                font: 10pt 'Segoe UI';
                padding: 2px 18px;
                letter-spacing: 0.5px;
            }}
        """)
        return badge
