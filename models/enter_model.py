class EnterModel:
    def __init__(self, db_name="gym.db"):
        self.db_name = db_name

    @staticmethod
    def validate(name):
        if not name:
            return False
        return True