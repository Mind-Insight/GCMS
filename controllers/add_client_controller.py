class AddClientController:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.ui.addClientButton.clicked.connect(self.handle_create_client)

    def handle_create_client(self):
        title = self.view.ui.comboBoxMembership.currentText().split(" - ")
        membership_id = self.model.get_membership_id_by_title(title)[0]
        name, surname, gender, email = (
            self.view.ui.nameAddEdit.text(),
            self.view.ui.surnameAddEdit.text(),
            self.view.ui.genderAddEdit.text(),
            self.view.ui.emailAddEdit.text(),
        )
        self.model.add_client(
            name,
            surname,
            membership_id,
            gender,
            email,
        )
        self.view.parent().fill_table()
        self.view.close()
