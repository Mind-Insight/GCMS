from models.add_admin_model import AddAdminModel


class AddAdminController:
    def __init__(self, view, app):
        self.view = view
        self.app = app
        self.model = AddAdminModel()

        self.view.ui.addAdminButton.clicked.connect(
            self.handle_add_admin_button
        )
        self.view.ui.backButton.clicked.connect(self.handle_back_button)

    def handle_back_button(self):
        self.app.switch_view(0)

    def handle_add_admin_button(self):
        name, surname, email, password = (
            self.view.ui.nameEdit.text(),
            self.view.ui.surnameEdit.text(),
            self.view.ui.loginEdit.text(),
            self.view.ui.passwordEdit.text(),
        )
        self.model.add_admin(name, surname, email, password)
        self.app.switch_view(0)
