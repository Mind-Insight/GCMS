from models.client_model import ClientModel

from views.dialogs.add_client_dialog import AddClientDialog
from controllers.add_client_controller import AddClientController


class ClientController:
    def __init__(self, view, app):
        self.model = ClientModel()
        self.view = view
        self.app = app

        self.view.ui.backButton.clicked.connect(self.handle_back_button)
        self.view.ui.addButton.clicked.connect(self.handle_add_client)

    def handle_back_button(self):
        self.app.switch_view(1)

    def handle_add_client(self):
        self.add_form = AddClientDialog(
            parent=self.view,
        )
        self.add_client_controller = AddClientController(
            self.add_form,
            self.model,
        )
        self.add_form.show()

    def get_all_clients(self):
        return self.model.get_all_clients()

    def delete_client(self, client_id):
        self.model.delete_client(client_id)
        return "Клиент удалён!"
