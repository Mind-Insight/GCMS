import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow

import views.client_view
import views.enter_view
import views.menu_view
import controllers.client_controller
import controllers.enter_controller
import controllers.menu_controller


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система управления клиентами тренажерного зала")
        self.setGeometry(100, 100, 500, 500)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.client_view = views.client_view.ClientView(self)
        self.enter_view = views.enter_view.EnterView(self)
        self.menu_view = views.menu_view.MenuView(self)
        self.client_controller = (
            controllers.client_controller.ClientController(
                self.client_view, self
            )
        )
        self.enter_controller = controllers.enter_controller.EnterController(
            self.enter_view, self
        )
        self.menu_controller = controllers.menu_controller.MenuController(
            self.menu_view,
            self,
        )
        self.stack.addWidget(self.enter_view)
        self.stack.addWidget(self.menu_view)
        self.stack.addWidget(self.client_view)
        self.stack.setCurrentIndex(0)

    def switch_view(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
