import sqlite3


class ClientModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_client(self, name, surname, membership_id, gender, email):
        query = """
            INSERT INTO clients (name, surname, membership_id, gender, email)
            VALUES (?, ?, ?, ?, ?)
        """
        with self.connection:
            self.connection.execute(
                query, (name, surname, membership_id, gender, email)
            )

    def get_membership_id_by_title(self, title):
        duration, membership_type = title
        query = """
            SELECT membership_id FROM memberships
            JOIN membership_types ON type_id = membership_type_id
            WHERE type = ? AND duration = ?
        """
        response = self.cursor.execute(
            query, (membership_type, duration)
        ).fetchone()
        return response[0] if response else None

    def get_membership_duration_type(self):
        query = """
            SELECT duration, type
            FROM memberships
            JOIN membership_types ON type_id = membership_type_id
        """
        return self.cursor.execute(query).fetchall()

    def get_membership_duration_type_by_id(self, pk):
        query = """
            SELECT duration, type
            FROM memberships
            JOIN membership_types ON type_id = membership_type_id
            WHERE membership_id = ?
        """
        response = self.cursor.execute(query, (pk,)).fetchone()
        return response if response else None

    def update_client(
        self, client_id, name, surname, membership_id, gender, email
    ):
        query = """
            UPDATE clients
            SET name = ?, surname = ?, membership_id = ?, gender = ?, email = ?
            WHERE client_id = ?
        """
        with self.connection:
            self.cursor.execute(
                query, (name, surname, membership_id, gender, email, client_id)
            )

    def delete_clients(self, client_ids):
        placeholder = ", ".join(["?"] * len(client_ids))
        query = f"DELETE FROM clients WHERE client_id IN ({placeholder})"
        with self.connection:
            self.cursor.execute(query, client_ids)

    def get_client_id_by_row(self, row):
        clients = self.get_all_clients()
        return clients[row][0] if row < len(clients) else None

    def get_all_memberships(self):
        query = "SELECT * FROM memberships"
        return self.cursor.execute(query).fetchall()

    def get_all_clients(self):
        query = "SELECT * FROM clients"
        return self.cursor.execute(query).fetchall()

    def get_all_clients_except_id_field(self):
        query = """
            SELECT name, surname, membership_id, gender, email
            FROM clients
        """
        return self.cursor.execute(query).fetchall()

    def get_client_by_id(self, client_id):
        query = """
            SELECT * FROM clients
            WHERE client_id = ?
        """
        response = self.cursor.execute(query, (client_id,)).fetchone()
        return response if response else None

    def get_cursor_headers(self):
        return self.cursor.description

    def __del__(self):
        """Закрытие соединения при уничтожении объекта."""
        self.connection.close()
