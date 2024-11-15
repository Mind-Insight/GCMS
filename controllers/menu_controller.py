from models.menu_model import MenuModel


class MenuController:
    def __init__(self, view, app):
        self.model = MenuModel()
        self.view = view
        self.app = app

        self.view.ui.clientsButton.clicked.connect(self.handle_clients_button)

    def handle_clients_button(self):
        self.app.switch_view(2)
