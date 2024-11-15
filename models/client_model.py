import sqlite3


class ClientModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # self.create_table()

    def add_client(self, name, surname, membership_id, gender, email):
        query = """
            INSERT INTO clients
            (name, surname, membership_id, gender, email)
            VALUES (?, ?, ?, ?, ?)
        """
        self.connection.execute(
            query, (name, surname, membership_id, gender, email)
        )
        self.connection.commit()

    def get_membership_id_by_title(self, title):
        duration, membership_type = title
        response = self.cursor.execute(
            f"""
                SELECT membership_id FROM memberships
                JOIN membership_types
                ON type_id = membership_id
                WHERE type = '{membership_type}'
                AND duration = '{duration}'
            """
        ).fetchone()
        return response

    def get_membership_duration_type(self):
        response = self.cursor.execute(
            """
                SELECT duration, type
                FROM memberships
                JOIN membership_types
                ON type_id = membership_type_id
            """
        ).fetchall()
        return response

    def get_all_memberships(self):
        response = self.cursor.execute("SELECT * FROM memberships").fetchall()
        return response

    def get_all_clients(self):
        response = self.cursor.execute("SELECT * FROM clients").fetchall()
        return response

    def get_cursor_headers(self):
        return self.cursor.description[:-2]
