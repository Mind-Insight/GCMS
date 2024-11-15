import sqlite3


class ClientModel:
    def __init__(self, db_name="gym.db"):
        self.conn = sqlite3.connect(db_name)
        # self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_client(self, name, phone, email):
        query = "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, phone, email))
        self.conn.commit()

    def get_all_clients(self):
        query = "SELECT * FROM clients"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def delete_client(self, client_id):
        query = "DELETE FROM clients WHERE id = ?"
        self.conn.execute(query, (client_id,))
        self.conn.commit()
