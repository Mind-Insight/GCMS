from PyQt6.QtWidgets import QMainWindow

from ui.ui_enter import Ui_EnterWindow


class EnterView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_EnterWindow()
        self.ui.setupUi(self)
