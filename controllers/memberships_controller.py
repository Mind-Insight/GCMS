class MembershipController:
    def __init__(self, view, app):
        self.view = view
        self.app = app

        self.view.ui.backButton.clicked.connect(self.handle_back_button)

    def handle_back_button(self):
        self.app.switch_view(1)
