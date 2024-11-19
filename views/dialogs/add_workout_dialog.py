from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtCore import Qt

from ui.dialogs.ui_add_workout import Ui_AddWorkout
from models.workout_model import WorkoutModel
from models.client_model import ClientModel


class AddWorkoutDialog(QMainWindow):
    def __init__(self, parent=None, workout_data=None):
        super().__init__(parent)
        self.model = WorkoutModel()
        self.clients_model = ClientModel()
        self.ui = Ui_AddWorkout()
        self.ui.setupUi(self)
        self.add_clients()
        self.fill_trianers()
        self.fill_workout_types()

    def add_clients(self):
        clients = self.clients_model.get_all_clients()
        for client in clients:
            item = QListWidgetItem(f"{client[1]} {client[2]}")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.listWidget.addItem(item)

    def fill_workout_types(self):
        for workout_type in self.model.get_all_workout_types():
            self.ui.comboBoxWorkoutType.addItem(workout_type[0])

    def fill_trianers(self):
        for name, surname in self.model.get_all_trainers():
            self.ui.comboBoxTrainers.addItem(f"{name} {surname}")

    def get_selected_clients(self):
        selected_clients = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                client_id = self.clients_model.get_client_by_name_surname(
                    *(item.data(0).split())
                )
                selected_clients.append(client_id)
        return selected_clients

    def set_selected_clients(self, client_ids):
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            client_id = self.clients_model.get_client_by_name_surname(
                *(item.data(0).split())
            )
            if client_id in client_ids:
                item.setCheckState(Qt.CheckState.Checked)
