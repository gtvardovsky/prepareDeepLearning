from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout
from UI import constsettingswidget_ui


class ConstSettingsWidget(QWidget, constsettingswidget_ui.Ui_ConstSettingsWidget):
    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле constsettingswidget_ui.py
        super().__init__()
        # Инициализация дизайна
        self.init_UI()

    def init_UI(self):
        self.setupUi(self)
        # Создание радио-кнопок
        self.mImageRadio = QRadioButton('Изображения')
        self.mVideoRadio = QRadioButton('Видео файл')
        self.mWebCamRadio = QRadioButton('Web-камера')

        # Создание вертикального layout, добавление на него радио-кнопок и установка layout на виджет
        vertical_box = QVBoxLayout()
        vertical_box.addWidget(self.mImageRadio)
        vertical_box.addWidget(self.mVideoRadio)
        vertical_box.addWidget(self.mWebCamRadio)
        vertical_box.addStretch(1)
        self.inputChanged_gb.setLayout(vertical_box)

        # Изначально выбрано изображение
        self.mImageRadio.setChecked(True)


