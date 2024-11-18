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
        print(self.workout_id)
        info = self.model.get_training_info_by_id(self.workout_id)
        print(info)
        trainer = self.model.get_trainer_by_id(info[3])
        self.ui.trainingType.setText(self.workout_info[0])
        self.ui.trainer.setText(" ".join(trainer))
        self.ui.dateAndTime.setText(" ".join([info[-2], info[-1]]))
