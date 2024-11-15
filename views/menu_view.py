from PyQt6.QtWidgets import QMainWindow

from ui.ui_menu import Ui_MenuWindow


class MenuView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

