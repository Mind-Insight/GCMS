from PyQt6.QtCore import QDate, QTime


class AddWorkoutController:
    def __init__(self, view, model, workout_id=None):
        self.view = view
        self.model = model
        self.workout_id = workout_id
        self.view.ui.addWorkoutButton.clicked.connect(self.handle_save_workout)

        if self.workout_id is not None:
            self.load_workout_data()

    def load_workout_data(self):
        workout = self.model.get_training_info_by_id(self.workout_id)
        related_clients = self.model.get_related_client_ids_by_workout_id(
            self.workout_id
        )
        workout_type = self.model.get_workout_type_by_id(workout[1])
        trainer = self.model.get_trainer_by_id(workout[2])
        self.view.ui.comboBoxWorkoutType.setCurrentText(workout_type)
        self.view.ui.comboBoxTrainers.setCurrentText(
            f"{trainer[0]} {trainer[1]}"
        )
        self.view.ui.dateEdit.setDate(
            QDate.fromString(workout[-2], "yyyy-MM-dd")
        )
        self.view.ui.timeEdit.setTime(
            QTime.fromString(workout[-1], "HH:mm:ss")
        )
        self.view.set_selected_clients(related_clients)

    def handle_save_workout(self):
        workout_type = self.model.workout_type_id_by_type(
            self.view.ui.comboBoxWorkoutType.currentText()
        )
        trainer = self.model.get_trainer_by_name_surname(
            *(self.view.ui.comboBoxTrainers.currentText().split())
        )
        date = self.view.ui.dateEdit.text()
        time = self.view.ui.timeEdit.text()
        client_ids = self.view.get_selected_clients()

        if self.workout_id is None:
            self.model.add_workout(
                workout_type, date, time, trainer, client_ids
            )
        else:
            self.model.update_workout(
                self.workout_id, workout_type, date, time, trainer, client_ids
            )

        self.view.parent().fill()
        self.view.close()
