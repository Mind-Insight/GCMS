import sqlite3


class ClientModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # self.create_table()

    def add_client(self, name, phone, email):
        query = "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, phone, email))
        self.conn.commit()

    def get_all_clients(self):
        response = self.cursor.execute("SELECT * FROM clients").fetchall()
        return response

    def get_cursor_headers(self):
        return self.cursor.description[:-2]
