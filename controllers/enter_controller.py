from models.enter_model import EnterModel


class EnterController:
    def __init__(self, view, app):
        self.model = EnterModel()
        self.view = view
        self.app = app

        self.view.ui.enterButton.clicked.connect(self.handle_enter_button)

    def handle_enter_button(self):
        name = self.view.ui.loginEdit.text()
        is_valid = self.model.validate(name)
        print(is_valid)
        if is_valid:
            self.app.switch_view(1)
