from models.workout_model import WorkoutModel


class AddWorkoutController:
    def __init__(self, view):
        self.view = view
        self.model = WorkoutModel()
        self.view.ui.addWorkoutButton.clicked.connect(self.handle_save_workout)

    def handle_save_workout(self):
        workout_type = self.view.ui.comboBoxWorkoutType.currentText()
        print(self.view.ui.comboBoxTrainers.currentText())
        trainer = self.model.get_trainer_by_name_surname(
            *(self.view.ui.comboBoxTrainers.currentText().split())
        )
        date = self.view.ui.dateEdit.text()
        time = self.view.ui.timeEdit.text()
        client_ids = self.view.get_selected_clients()

        if not workout_type or not trainer or not client_ids:
            self.view.show_error("Все поля должны быть заполнены!")
            return

        self.model.add_workout(workout_type, date, time, trainer, client_ids)
