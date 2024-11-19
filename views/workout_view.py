from PyQt6.QtWidgets import QMainWindow, QListWidgetItem

from ui.ui_workouts import Ui_WorkoutDialog
from models.workout_model import WorkoutModel


class WorkoutView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = WorkoutModel()
        self.ui = Ui_WorkoutDialog()
        self.ui.setupUi(self)
        self.fill()

    def fill(self):
        self.ui.listWidget.clear()
        response = self.model.get_all_workouts()
        for training in response:
            workout_type = self.model.get_workout_type_by_id(training[1])
            item_text = f"{workout_type} - {training[-2]} - {training[-1]}"
            item = QListWidgetItem(item_text)
            item.setData(1, training[0])
            self.ui.listWidget.addItem(item)
