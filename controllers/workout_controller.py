from views.dialogs.add_workout_dialog import AddWorkoutDialog
from views.dialogs.workout_details import WorkoutDetailsDialog
from controllers.add_workout_controller import AddWorkoutController


class WorkoutController:
    def __init__(self, view, app):
        super().__init__()
        self.view = view
        self.app = app

        self.view.ui.addWorkoutButton.clicked.connect(
            self.handle_add_workout_button
        )
        self.view.ui.listWidget.itemDoubleClicked.connect(
            self.get_training_info
        )

    def handle_add_workout_button(self):
        self.dialog = AddWorkoutDialog(self.view)
        self.controller = AddWorkoutController(self.dialog)
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
