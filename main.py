import sys
from PyQt6.QtWidgets import (
    QApplication,
    QStackedWidget,
    QMainWindow,
)

import views.client_view
import views.enter_view
import controllers.client_controller
import controllers.enter_controller


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система управления тренажерным залом")
        self.setGeometry(100, 100, 500, 500)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.client_controller = (
            controllers.client_controller.ClientController()
        )
        self.enter_controller = controllers.enter_controller.EnterController()
        self.client_view = views.client_view.ClientView(self.client_controller)
        self.enter_view = views.enter_view.EnterView(self.enter_controller)
        self.stack.addWidget(self.enter_view)
        self.stack.addWidget(self.client_view)
        self.init_navigation()

    def init_navigation(self):
        self.enter_view.ui.enterButton.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = MainApp()
    obj.show()
    sys.exit(app.exec())
