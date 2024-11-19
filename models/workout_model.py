import sqlite3


class WorkoutModel:
    def __init__(self, db_name="gym.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_all_workout_types(self):
        query = "SELECT workout_type FROM workout_types"
        return self.cursor.execute(query).fetchall()

    def get_all_trainers(self):
        query = "SELECT name, middle_name FROM trainers"
        return self.cursor.execute(query).fetchall()

    def get_all_workouts(self):
        query = "SELECT * FROM workouts"
        return self.cursor.execute(query).fetchall()

    def get_workout_type_by_id(self, workout_type_id):
        query = """
            SELECT workout_type
            FROM workout_types
            WHERE workout_type_id = ?
        """
        response = self.cursor.execute(query, (workout_type_id,)).fetchone()
        return response[0] if response else None

    def get_trainer_by_id(self, trainer_id):
        query = """
            SELECT name, middle_name
            FROM trainers
            WHERE trainer_id = ?
        """
        response = self.cursor.execute(query, (trainer_id,)).fetchone()
        return response if response else None

    def get_training_info_by_id(self, workout_id):
        query = "SELECT * FROM workouts WHERE workout_id = ?"
        response = self.cursor.execute(query, (workout_id,)).fetchone()
        return response if response else None

    def get_related_clients_by_id(self, workout_id):
        query = """
            SELECT name, surname
            FROM clients
            JOIN workout_clients
            ON clients.client_id = workout_clients.client_id
            WHERE workout_clients.workout_id = ?
        """
        return self.cursor.execute(query, (workout_id,)).fetchall()

    def get_related_client_ids_by_workout_id(self, workout_id):
        query = """
            SELECT client_id
            FROM workout_clients
            WHERE workout_id = ?
        """
        return self.cursor.execute(query, (workout_id,)).fetchall()

    def get_trainer_by_name_surname(self, name, surname):
        query = """
            SELECT trainer_id
            FROM trainers
            WHERE name = ? AND middle_name = ?
        """
        response = self.cursor.execute(query, (name, surname)).fetchone()
        return response[0] if response else None

    def add_workout(self, workout_type_id, date, time, trainer_id, client_ids):
        query_workout = """
            INSERT INTO workouts (workout_type, trainer_id, date, time)
            VALUES (?, ?, ?, ?)
        """
        with self.connection:
            self.cursor.execute(
                query_workout, (workout_type_id[0], trainer_id, date, time)
            )
            workout_id = self.cursor.lastrowid

            query_clients = """
                INSERT INTO workout_clients (workout_id, client_id)
                VALUES (?, ?)
            """
            self.cursor.executemany(
                query_clients,
                [(workout_id, client_id[0]) for client_id in client_ids],
            )

    def workout_type_id_by_type(self, workout_type):
        query = """
            SELECT workout_type_id
            FROM workout_types
            WHERE workout_type = ?
        """
        response = self.cursor.execute(query, (workout_type,)).fetchone()
        return response

    def delete_workout(self, workout_id):
        query = "DELETE FROM workouts WHERE workout_id = ?"
        self.cursor.execute(query, (workout_id,))
        self.connection.commit()

    def update_workout(
        self, workout_id, workout_type_id, date, time, trainer_id, client_ids
    ):
        query_update_workout = """
            UPDATE workouts
            SET workout_type = ?, date = ?, time = ?, trainer_id = ?
            WHERE workout_id = ?
        """
        self.cursor.execute(
            query_update_workout,
            (workout_type_id[0], date, time, trainer_id, workout_id),
        )
        query_delete_clients = (
            "DELETE FROM workout_clients WHERE workout_id = ?"
        )
        self.cursor.execute(query_delete_clients, (workout_id,))

        query_insert_clients = """
            INSERT INTO workout_clients (workout_id, client_id)
            VALUES (?, ?)
        """
        self.cursor.executemany(
            query_insert_clients,
            [(workout_id, client_id[0]) for client_id in client_ids],
        )

        self.connection.commit()

    def __del__(self):
        self.connection.close()
