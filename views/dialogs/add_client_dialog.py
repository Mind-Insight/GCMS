from PyQt6.QtWidgets import QMainWindow

from models.client_model import ClientModel
from ui.dialogs.ui_add_client_dialog import Ui_AddClientDialog


class AddClientDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = ClientModel()
        self.ui = Ui_AddClientDialog()
        self.ui.setupUi(self)
        self.fill_comboBox()

    def fill_comboBox(self):
        memberships = self.model.get_membership_duration_type()
        self.ui.comboBoxMembership.addItems(
            [f"{item[0]} - {item[1]}" for item in memberships]
        )
