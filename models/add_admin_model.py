import sqlite3


class AddAdminModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def add_admin(self, name, surname, email, password, photo_data):
        query = """
                INSERT INTO admins (name, surname, email, password, photo)
                VALUES (?, ?, ?, ?, ?)
            """
        self.cursor.execute(
            query,
            (
                name,
                surname,
                email,
                password,
                photo_data,
            ),
        )
        self.connection.commit()
