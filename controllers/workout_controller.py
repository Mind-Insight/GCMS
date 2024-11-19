from PyQt6.QtWidgets import QMessageBox

from views.dialogs.add_workout_dialog import AddWorkoutDialog
from views.dialogs.workout_details import WorkoutDetailsDialog
from controllers.add_workout_controller import AddWorkoutController
from models.workout_model import WorkoutModel


class WorkoutController:
    def __init__(self, view, app):
        self.model = WorkoutModel()
        self.view = view
        self.app = app

        self.view.ui.backButton.clicked.connect(self.handle_back_button)
        self.view.ui.addWorkoutButton.clicked.connect(self.handle_add_workout)
        self.view.ui.changeWorkoutButton.clicked.connect(
            self.handle_edit_workout
        )
        self.view.ui.deleteWorkoutButton.clicked.connect(
            self.handle_delete_workout
        )
        self.view.ui.listWidget.itemDoubleClicked.connect(
            self.get_training_info
        )

    def handle_back_button(self):
        self.app.switch_view(1)

    def handle_add_workout(self):
        self.open_workout_dialog()

    def handle_edit_workout(self):
        selected_row = self.view.ui.listWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self.view, "Ошибка", "Выберите тренировку для изменения!"
            )
            return

        workout_id = self.view.ui.listWidget.item(selected_row).data(1)
        workout_data = self.model.get_training_info_by_id(workout_id)
        self.open_workout_dialog(workout_data)

    def handle_delete_workout(self):
        selected_row = self.view.ui.listWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self.view, "Ошибка", "Выберите тренировку для удаления!"
            )
            return

        workout_id = self.view.ui.listWidget.item(selected_row).data(1)
        confirmation = QMessageBox.question(
            self.view,
            "Подтвердить удаление",
            f"Вы уверены, что хотите удалить тренировку ID: {workout_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirmation == QMessageBox.StandardButton.Yes:
            self.model.delete_workout(workout_id)
            self.view.fill()

    def open_workout_dialog(self, workout_data=None):
        self.dialog = AddWorkoutDialog(
            parent=self.view,
            workout_data=workout_data,
        )
        self.add_workout_controller = AddWorkoutController(
            self.dialog,
            self.model,
            workout_data[0] if workout_data else None,
        )
        self.dialog.show()

    def get_training_info(self, item):
        workout_id = item.data(1)
        workout_info = item.data(0).split(" - ")
        self.dialog = WorkoutDetailsDialog(
            parent=self.view,
            workout_id=workout_id,
            workout_info=workout_info,
        )
        self.dialog.show()
