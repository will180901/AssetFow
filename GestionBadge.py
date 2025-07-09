from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class GestionBadge:
    @staticmethod
    def creer_badge_role(role):
        """Crée un badge stylisé et coloré selon le rôle de l'utilisateur."""
        badge = QLabel(role)
        badge.setAlignment(Qt.AlignCenter)
        badge.setMinimumHeight(28)
        badge.setMaximumHeight(32)
        badge.setFixedWidth(110)  # Largeur fixe à 110px
        badge.setMargin(0)
        badge.setContentsMargins(0, 0, 0, 0)

        # Normalisation du rôle pour la correspondance
        role_normalise = role.strip().lower()
        # Dictionnaire de correspondance flexible
        mapping = {
            "admin": "Admin",
            "administrateur": "Admin",
            "technicien": "Technicien",
            "superviseur": "Superviseur",
            "utilisateur": "Utilisateur",
            "user": "Utilisateur"
        }
        role_cle = mapping.get(role_normalise, "Utilisateur")

        # Palette moderne et professionnelle
        styles = {
            "Admin": {
                "bg": "rgba(255, 59, 48, 0.12)",
                "color": "#FF3B30",
                "border": "#FF3B30"
            },
            "Technicien": {
                "bg": "rgba(0, 122, 255, 0.12)",
                "color": "#007AFF",
                "border": "#007AFF"
            },
            "Superviseur": {
                "bg": "rgba(255, 149, 0, 0.12)",
                "color": "#FF9500",
                "border": "#FF9500"
            },
            "Utilisateur": {
                "bg": "rgba(60, 60, 67, 0.08)",
                "color": "#3C3C43",
                "border": "#B0B0B0"
            }
        }
        style = styles.get(role_cle, styles["Utilisateur"])
        badge.setStyleSheet(f"""
            QLabel {{
                background-color: {style['bg']};
                color: {style['color']};
                border: 1px solid {style['border']};
                border-radius: 12px;
                padding: 2px 0px;
                font: 600 10pt 'Segoe UI', 'Bahnschrift', Arial, sans-serif;
                letter-spacing: 0.5px;
            }}
        """)
        return badge
