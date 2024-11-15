from PyQt6.QtWidgets import QMainWindow

from models.client_model import ClientModel
from ui.dialogs.ui_add_client_dialog import Ui_AddClientDialog


class AddClientDialog(QMainWindow):
    def __init__(self, parent=None, client_data=None):
        super().__init__(parent)
        self.model = ClientModel()
        self.ui = Ui_AddClientDialog()
        self.ui.setupUi(self)
        self.fill_comboBox()
        if client_data:
            self.ui.label.setText("Изменить клиента")
            self.ui.addClientButton.setText("Изменить")
            self.fill_fields(client_data)

    def fill_fields(self, client_data):
        self.ui.nameAddEdit.setText(client_data[1])
        self.ui.surnameAddEdit.setText(client_data[2])
        self.ui.genderAddEdit.setText(client_data[4])
        self.ui.emailAddEdit.setText(client_data[5])

        membership_title = " - ".join(
            self.model.get_membership_duration_type_by_id(client_data[3])
        )
        index = self.ui.comboBoxMembership.findText(membership_title)
        if index != -1:
            self.ui.comboBoxMembership.setCurrentIndex(index)

    def fill_comboBox(self):
        memberships = self.model.get_membership_duration_type()
        self.ui.comboBoxMembership.addItems(
            [f"{item[0]} - {item[1]}" for item in memberships]
        )
