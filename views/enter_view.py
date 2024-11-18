from PyQt6.QtWidgets import QMainWindow

from ui.ui_enter import Ui_EnterWindow


class EnterView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EnterWindow()
        self.ui.setupUi(self)
