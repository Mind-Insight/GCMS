class AddClientController:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.ui.addClientButton.clicked.connect(self.handle_create_client)

    def handle_create_client(self):
        title = self.view.ui.comboBoxMembership.currentText().split(" - ")
        membership_id = self.model.get_membership_id_by_title(title)
        print(membership_id)