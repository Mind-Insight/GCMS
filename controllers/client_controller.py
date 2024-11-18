from PyQt6.QtWidgets import QMessageBox

from models.client_model import ClientModel
from views.dialogs.add_client_dialog import AddClientDialog
from controllers.add_client_controller import AddClientController


class ClientController:
    def __init__(self, view, app):
        self.model = ClientModel()
        self.view = view
        self.app = app

        self.view.ui.backButton.clicked.connect(self.handle_back_button)
        self.view.ui.addButton.clicked.connect(self.handle_add_client)
        self.view.ui.changeButton.clicked.connect(self.handle_edit_client)
        self.view.ui.deleteButton.clicked.connect(self.handle_delete_client)

    def handle_back_button(self):
        self.app.switch_view(1)

    def handle_add_client(self):
        self.open_client_dialog()

    def handle_edit_client(self):
        selected_row = self.view.ui.tableWidget.currentRow()
        client_id = self.model.get_all_clients()[selected_row][0]
        client_data = self.model.get_client_by_id(client_id)
        self.open_client_dialog(client_data)

    def handle_delete_client(self):
        selected_indexes = self.view.ui.tableWidget.selectedIndexes()
        selected_rows = sorted(set(index.row() for index in selected_indexes))
        confirmation = QMessageBox.question(
            self.view,
            "Подтвердить удаление",
            "Вы уверены, что хотите удалить записи: "
            f"{", ".join(map(lambda x: str(x + 1), selected_rows))}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirmation == QMessageBox.StandardButton.Yes:
            client_ids_to_delete = []
            for row in selected_rows:
                client_id = self.model.get_client_id_by_row(row)
                client_ids_to_delete.append(client_id)
            self.model.delete_clients(client_ids_to_delete)
            self.view.fill_table()

    def open_client_dialog(self, client_data=None):
        self.dialog = AddClientDialog(
            parent=self.view,
            client_data=client_data,
        )
        self.add_client_controller = AddClientController(
            self.dialog, self.model, client_data[0] if client_data else None
        )
        self.dialog.show()
