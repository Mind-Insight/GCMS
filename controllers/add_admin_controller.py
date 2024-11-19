import os
import base64

from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap

from models.add_admin_model import AddAdminModel


class AddAdminController:
    def __init__(self, view, app):
        self.view = view
        self.app = app
        self.model = AddAdminModel()

        self.view.ui.addAdminButton.clicked.connect(
            self.handle_add_admin_button
        )
        self.view.ui.backButton.clicked.connect(self.handle_back_button)
        self.view.ui.uploadImageButton.clicked.connect(
            self.handle_upload_image
        )

    def handle_back_button(self):
        self.app.switch_view(0)

    def handle_add_admin_button(self):
        name, surname, email, password = (
            self.view.ui.nameEdit.text(),
            self.view.ui.surnameEdit.text(),
            self.view.ui.loginEdit.text(),
            self.view.ui.passwordEdit.text(),
        )
        photo_data = None
        if hasattr(self.view, "selected_image_path") and os.path.exists(
            self.view.selected_image_path
        ):
            with open(self.view.selected_image_path, "rb") as file:
                photo_data = base64.b64encode(file.read())
        self.model.add_admin(name, surname, email, password, photo_data)
        self.app.switch_view(0)

    def handle_upload_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(
            self.view,
            "Выбрать изображение",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg)",
        )
        if image_path:
            self.view.ui.imageLabel.setPixmap(QPixmap(image_path))
            self.view.selected_image_path = image_path
