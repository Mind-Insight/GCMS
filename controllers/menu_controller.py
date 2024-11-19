from models.menu_model import MenuModel


class MenuController:
    def __init__(self, view, app):
        self.model = MenuModel()
        self.view = view
        self.app = app

        self.view.ui.clientsButton.clicked.connect(self.handle_clients_button)
        self.view.ui.workoutsButton.clicked.connect(
            self.handle_workouts_button
        )
        self.view.ui.memebershipsButton.clicked.connect(
            self.handle_memberships_button
        )
        self.view.ui.exitButton.clicked.connect(self.handle_exit_button)

    def handle_clients_button(self):
        self.app.switch_view(2)

    def handle_workouts_button(self):
        self.app.switch_view(4)

    def handle_exit_button(self):
        self.app.enter_view.ui.emailEdit.clear()
        self.app.enter_view.ui.passwordEdit.clear()
        self.app.enter_view.ui.errorLabel.clear()

        self.app.switch_view(0)
    
    def handle_memberships_button(self):
        self.app.switch_view(5)
