import sqlite3


class EnterModel:
    def __init__(self, db_name="gym.db"):
        self.db_name = db_name
        self.connect_to_database()

    def connect_to_database(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    @staticmethod
    def validate_fields(email, password):
        if not email and not password:
            return (False, "поля должны быть заполнены")
        if not email and password:
            return (False, "поле email не может быть пустым")
        if not password and email:
            return (False, "поле password не может быть пустым")
        return (True, "success")

    def check_admin_in_database(self, email, password):
        response = self.cursor.execute(
            f"""
                SELECT * FROM admins
                WHERE email = '{email}'
                AND password = '{password}'
            """
        ).fetchone()
        return response
