from models.menu_model import MenuModel


class MenuController:
    def __init__(self, view, app):
        self.model = MenuModel()
        self.view = view
        self.app = app

        self.view.ui.backButton.clicked.connect(self.handle_back_button)
        self.view.ui.clientsButton.clicked.connect(self.handle_clients_button)
        self.view.ui.workoutsButton.clicked.connect(
            self.handle_workouts_button
        )

    def handle_back_button(self):
        self.app.switch_view(0)

    def handle_clients_button(self):
        self.app.switch_view(2)

    def handle_workouts_button(self):
        self.app.switch_view(4)
