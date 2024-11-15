import sqlite3


class EnterModel:
    def __init__(self, db_name="gym.db"):
        self.db_name = db_name