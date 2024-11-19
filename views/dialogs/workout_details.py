from PyQt6.QtWidgets import QMainWindow

from ui.dialogs.ui_workout_detail_dialog import Ui_WorkoutDetailDialog
from models.workout_model import WorkoutModel


class WorkoutDetailsDialog(QMainWindow):
    def __init__(
        self,
        workout_id=None,
        workout_info=None,
        parent=None,
    ):
        super().__init__(parent)
        self.model = WorkoutModel()
        self.ui = Ui_WorkoutDetailDialog()
        self.ui.setupUi(self)
        self.workout_id, self.workout_info = workout_id, workout_info
        self.show_data()

    def show_data(self):
        info = self.model.get_training_info_by_id(self.workout_id)
        clients = self.model.get_related_clients_by_id(self.workout_id)
        result_clients = ""
        for name, surname in clients:
            result_clients = result_clients + f", {name} {surname}"
        self.ui.clients.setText(result_clients[2:])
        trainer = self.model.get_trainer_by_id(info[2])
        self.ui.trainingType.setText(self.workout_info[0])
        self.ui.trainer.setText(" ".join(trainer))
        self.ui.dateAndTime.setText(" ".join([info[-2], info[-1]]))
