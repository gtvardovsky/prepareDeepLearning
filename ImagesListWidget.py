from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout
from UI import imageslistwidget_ui


class ImagesListWidget(QWidget, imageslistwidget_ui.Ui_imagesListWidget):
    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле constsettingswidget_ui.py
        super().__init__()
        # Инициализация дизайна
        self.init_UI()

    def init_UI(self):
        self.setupUi(self)



