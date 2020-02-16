from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout
from UI import imageslistwidget_ui


class ImagesListWidget(QWidget, imageslistwidget_ui.Ui_imagesListWidget, ):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setupUi(self)



