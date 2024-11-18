from PyQt6.QtWidgets import QMainWindow

from ui.ui_add_admin import Ui_AddAdmin


class AddAdminView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddAdmin()
        self.ui.setupUi(self)