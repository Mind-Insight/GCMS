from PyQt6.QtWidgets import QMainWindow

from ui.ui_menu import Ui_MenuWindow


class MenuView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

