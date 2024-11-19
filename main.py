import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow

from views.client_view import ClientView
from views.enter_view import EnterView
from views.menu_view import MenuView
from views.add_admin_view import AddAdminView
from views.workout_view import WorkoutView
from views.membership_view import MembershipView
from controllers.workout_controller import WorkoutController
from controllers.memberships_controller import MembershipController
from controllers.add_admin_controller import AddAdminController
from controllers.client_controller import ClientController
from controllers.enter_controller import EnterController
from controllers.menu_controller import MenuController


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система управления клиентами тренажерного зала")
        self.setGeometry(100, 100, 500, 500)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.enter_view = EnterView()
        self.client_view = ClientView()
        self.menu_view = MenuView()
        self.add_admin_view = AddAdminView()
        self.workout_view = WorkoutView()
        self.membership_view = MembershipView()

        self.client_controller = ClientController(self.client_view, self)
        self.enter_controller = EnterController(self.enter_view, self)
        self.menu_controller = MenuController(
            self.menu_view,
            self,
        )
        self.add_admin_controller = AddAdminController(
            self.add_admin_view,
            self,
        )
        self.workout_controller = WorkoutController(self.workout_view, self)
        self.membership_controller = MembershipController(
            self.membership_view, self
        )

        self.stack.addWidget(self.enter_view)
        self.stack.addWidget(self.menu_view)
        self.stack.addWidget(self.client_view)
        self.stack.addWidget(self.add_admin_view)
        self.stack.addWidget(self.workout_view)
        self.stack.addWidget(self.membership_view)
        self.stack.setCurrentIndex(0)

    def switch_view(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
