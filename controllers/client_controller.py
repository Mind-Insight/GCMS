from models.client_model import ClientModel


class ClientController:
    def __init__(self):
        self.model = ClientModel()

    def add_client(self, name, phone, email):
        if not name:
            return "Имя не может быть пустым!"
        self.model.add_client(name, phone, email)
        return "Клиент добавлен успешно!"

    def get_all_clients(self):
        return self.model.get_all_clients()

    def delete_client(self, client_id):
        self.model.delete_client(client_id)
        return "Клиент удалён!"
