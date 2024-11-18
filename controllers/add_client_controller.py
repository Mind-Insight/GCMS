class AddClientController:
    def __init__(self, view, model, client_id=None):
        self.model = model
        self.view = view
        self.client_id = client_id
        self.view.ui.addClientButton.clicked.connect(self.handle_save_client)

    def handle_save_client(self):
        title = self.view.ui.comboBoxMembership.currentText().split(" - ")
        print(title)
        membership_id = self.model.get_membership_id_by_title(title)
        name, surname, gender, email = (
            self.view.ui.nameAddEdit.text(),
            self.view.ui.surnameAddEdit.text(),
            self.view.ui.genderAddEdit.text(),
            self.view.ui.emailAddEdit.text(),
        )
        if self.client_id is None:
            self.model.add_client(
                name,
                surname,
                membership_id,
                gender,
                email,
            )
        else:
            self.model.update_client(
                self.client_id,
                name,
                surname,
                membership_id,
                gender,
                email,
            )
        self.view.parent().fill_table()
        self.view.close()
