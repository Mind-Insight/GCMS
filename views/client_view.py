from PyQt6.QtWidgets import QMainWindow

from ui.ui_client import Ui_ClientsWindow


class ClientView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_ClientsWindow()
        self.ui.setupUi(self)
