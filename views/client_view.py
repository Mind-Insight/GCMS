from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from ui.ui_client import Ui_ClientsWindow
from models.client_model import ClientModel


class ClientView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.model = ClientModel()
        self.ui = Ui_ClientsWindow()
        self.ui.setupUi(self)
        self.fill_table()

    def fill_table(self):
        clients = self.model.get_all_clients()
        self.ui.tableWidget.setColumnCount(len(clients[0]))
        headers = self.model.get_cursor_headers()
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [item[0] for item in headers]
        )
        self.ui.tableWidget.setRowCount(len(clients))
        for i in range(len(clients)):
            for j in range(len(clients[i])):
                self.ui.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(clients[i][j]))
                )
