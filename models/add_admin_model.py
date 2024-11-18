import sqlite3


class AddAdminModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def add_admin(self, name, surname, email, password):
        self.cursor.execute(
            f"""
                INSERT INTO admins (name, surname, email, password)
                VALUES ('{name}', '{surname}', '{email}', '{password}')
            """
        )
        self.connection.commit()
