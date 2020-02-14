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
        mImage_radio = QRadioButton('Изображения')
        mVideo_radio = QRadioButton('Видео файл')
        mWebCam_radio = QRadioButton('Web-камера')

        # Создание вертикального layout, добавление на него радио-кнопок и установка layout на виджет
        vertical_box = QVBoxLayout()
        vertical_box.addWidget(mImage_radio)
        vertical_box.addWidget(mVideo_radio)
        vertical_box.addWidget(mWebCam_radio)
        vertical_box.addStretch(1)
        self.inputChanged_gb.setLayout(vertical_box)

        # Изначально выбрано изображение
        mImage_radio.setChecked(True)


