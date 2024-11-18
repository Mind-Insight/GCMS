from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QComboBox, QDateTimeEdit, QLabel
)
from PyQt6.QtCore import Qt, QDateTime


class AddWorkoutView(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Добавить тренировку")

        # Основной виджет и макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Поле для выбора типа тренировки
        self.type_label = QLabel("Тип тренировки:")
        self.layout.addWidget(self.type_label)

        self.workout_type_combo = QComboBox()
        self.workout_type_combo.addItems(["Кардио", "Силовая", "Йога", "Растяжка"])
        self.layout.addWidget(self.workout_type_combo)

        # Поле для выбора даты и времени
        self.date_time_label = QLabel("Дата и время тренировки:")
        self.layout.addWidget(self.date_time_label)

        self.date_time_edit = QDateTimeEdit()
        self.date_time_edit.setDateTime(QDateTime.currentDateTime())  # Устанавливаем текущее время
        self.date_time_edit.setCalendarPopup(True)  # Включаем всплывающее окно календаря
        self.layout.addWidget(self.date_time_edit)

        # Список клиентов с чекбоксами
        self.client_list = QListWidget()
        self.client_list.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.layout.addWidget(self.client_list)

        # Добавление клиентов в список
        self.add_clients(["Клиент 1", "Клиент 2", "Клиент 3", "Клиент 4"])

        # Кнопка для сохранения тренировки
        self.save_button = QPushButton("Сохранить тренировку")
        self.save_button.clicked.connect(self.save_workout)
        self.layout.addWidget(self.save_button)

    def add_clients(self, clients):
        """Добавляет клиентов в список с флажками."""
        for client in clients:
            item = QListWidgetItem(client)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.client_list.addItem(item)

    def get_selected_clients(self):
        """Возвращает список выбранных клиентов."""
        selected_clients = []
        for i in range(self.client_list.count()):
            item = self.client_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected_clients.append(item.text())
        return selected_clients

    def save_workout(self):
        """Сохраняет тренировку и возвращает в основной экран."""
        selected_clients = self.get_selected_clients()
        if not selected_clients:
            QMessageBox.warning(self, "Ошибка", "Выберите хотя бы одного клиента для тренировки.")
            return

        workout_type = self.workout_type_combo.currentText()
        date_time = self.date_time_edit.dateTime().toString("yyyy-MM-dd HH:mm")

        # Передаем данные в основной экран
        self.app.add_workout({
            "type": workout_type,
            "date_time": date_time,
            "clients": selected_clients
        })

        QMessageBox.information(self, "Успех", f"Тренировка сохранена!")
        self.close()  # Закрывает экран добавления тренировки
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QListWidgetItem
)


from PyQt6.QtWidgets import QListWidgetItem


class WorkoutListView(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Список тренировок")

        # Основной виджет и макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Список тренировок
        self.workout_list = QListWidget()
        self.layout.addWidget(self.workout_list)

        # Кнопка для добавления новой тренировки
        self.add_button = QPushButton("Добавить тренировку")
        self.add_button.clicked.connect(self.open_add_workout_screen)
        self.layout.addWidget(self.add_button)

        # Подключаем обработчик нажатия
        self.workout_list.itemClicked.connect(self.show_workout_details)

    def populate_workout_list(self, workouts):
        """Заполняет список тренировок."""
        self.workout_list.clear()
        for workout in workouts:
            item_text = f"{workout['type']} - {workout['date_time']}\nКлиенты: {', '.join(workout['clients'])}"
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, workout)  # Сохраняем данные тренировки
            self.workout_list.addItem(item)

    def open_add_workout_screen(self):
        """Открывает экран добавления тренировки."""
        self.app.show_add_workout_screen()

    def show_workout_details(self, item):
        """Открывает окно подробностей тренировки."""
        workout_data = item.data(Qt.ItemDataRole.UserRole)  # Получаем данные тренировки
        self.app.show_workout_details_screen(workout_data)

class App:
    def __init__(self):
        self.main_window = None
        self.add_workout_window = None
        self.details_window = None
        self.workouts = []  # Хранилище тренировок

    def show_main_window(self):
        """Показывает экран списка тренировок."""
        self.main_window = WorkoutListView(self)
        self.main_window.populate_workout_list(self.workouts)
        self.main_window.show()

    def show_add_workout_screen(self):
        """Показывает экран добавления тренировки."""
        if self.add_workout_window is None:
            self.add_workout_window = AddWorkoutView(self)
        self.add_workout_window.show()

    def show_workout_details_screen(self, workout_data):
        """Показывает окно подробностей тренировки."""
        self.details_window = WorkoutDetailsView(workout_data, parent=self.main_window)
        self.details_window.show()

    def add_workout(self, workout_data):
        """Добавляет тренировку и обновляет основной экран."""
        self.workouts.append(workout_data)
        if self.main_window:
            self.main_window.populate_workout_list(self.workouts)

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton


class WorkoutDetailsView(QMainWindow):
    def __init__(self, workout_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Подробности тренировки")

        # Основной виджет и макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Отображение информации о тренировке
        self.layout.addWidget(QLabel(f"Тип тренировки: {workout_data['type']}"))
        self.layout.addWidget(QLabel(f"Дата и время: {workout_data['date_time']}"))
        self.layout.addWidget(QLabel(f"Клиенты: {', '.join(workout_data['clients'])}"))

        # Кнопка закрытия
        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

if __name__ == "__main__":
    app = QApplication([])

    application = App()
    application.show_main_window()

    app.exec()
