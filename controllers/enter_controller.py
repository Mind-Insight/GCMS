from models.enter_model import EnterModel


class EnterController:
    def __init__(self, view, app):
        self.model = EnterModel()
        self.view = view
        self.app = app

        self.view.ui.enterButton.clicked.connect(self.handle_enter_button)
        self.view.ui.pushButton.clicked.connect(self.handle_add_admin_button)

    def handle_enter_button(self):
        email = self.view.ui.emailEdit.text()
        password = self.view.ui.passwordEdit.text()
        is_valid, verdict = self.model.validate_fields(
            email,
            password,
        )
        response = self.model.check_admin_in_database(email, password)
        if not is_valid:
            self.view.ui.errorLabel.setText(verdict)
        elif is_valid and not response:
            self.view.ui.errorLabel.setText("админ не найден")
        else:
            self.app.switch_view(1)

    def handle_add_admin_button(self):
        self.app.switch_view(3)
