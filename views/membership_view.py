from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from ui.ui_memberships import Ui_MembershipsDialog
from models.client_model import ClientModel


class MembershipView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MembershipsDialog()
        self.ui.setupUi(self)
        self.model = ClientModel()
        self.fill()

    def fill(self):
        memberships = self.model.get_all_memberships()
        self.ui.membershipTableWidget.setColumnCount(
            len(memberships[0]) if memberships else 0
        )
        headers = self.model.get_cursor_headers()
        self.ui.membershipTableWidget.setHorizontalHeaderLabels(
            [item[0] for item in headers]
        )
        self.ui.membershipTableWidget.setRowCount(len(memberships))
        for i in range(len(memberships)):
            for j in range(len(memberships[i])):
                self.ui.membershipTableWidget.setItem(
                    i, j, QTableWidgetItem(str(memberships[i][j]))
                )
