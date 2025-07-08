class NavigationManager:
    def __init__(self, ui):
        self.ui = ui
        self.setup_navigation()
        self.update_button_styles(self.ui.page_tableau_de_bord)

    def setup_navigation(self):

        self.nav_buttons = {
            self.ui.btn_bar_nav_tableau_de_bord: self.ui.page_tableau_de_bord,
            self.ui.btn_bar_nav_equipement: self.ui.page_equipement,
            self.ui.btn_bar_nav_tickets: self.ui.page_tickets,
            self.ui.btn_bar_nav_utilisateurs: self.ui.page_utilisateurs
        }

        for button, page in self.nav_buttons.items():
            button.clicked.connect(lambda _, p=page: self.show_page(p))

        self.ui.btn_icon_return_tableau_de_bord.clicked.connect(
            lambda: self.show_page(self.ui.page_tableau_de_bord))

    def show_page(self, page):
        """Affiche la page spécifiée dans le stackedWidget"""
        index = self.ui.stackedWidget.indexOf(page)
        self.ui.stackedWidget.setCurrentIndex(index)
        self.update_button_styles(page)

    def update_button_styles(self, active_page):
        """Met à jour le style des boutons pour indiquer la page active"""
        for button, page in self.nav_buttons.items():
            button.setProperty("active", page == active_page)
            button.style().unpolish(button)
            button.style().polish(button)
