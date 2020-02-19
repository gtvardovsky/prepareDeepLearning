from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout
from UI import imageslistwidget_ui
from ImageListProcessing import ImageListProcessing
from CommonState import COLOR_IMAGE


class ImagesListWidget(QWidget, imageslistwidget_ui.Ui_imagesListWidget):
    def __init__(self, processing: ImageListProcessing):
        super().__init__()
        self.init_UI()
        self.color_b.clicked.connect(self.colorBtnClicked)
        self.m_processing = processing
        self.previousImage_b.clicked.connect(self.m_processing.onPreviousButtonPress)
        self.nextImage_b.clicked.connect(self.m_processing.onNextButtonPress)

    def colorBtnClicked(self):
        if self.color_b.text() == 'COLOR':
            self.color_b.setText('GRAY')
            self.m_processing.setColor(COLOR_IMAGE['COLOR'])
        else:
            self.color_b.setText('COLOR')
            self.m_processing.setColor(COLOR_IMAGE['GRAY'])

    def init_UI(self):
        self.setupUi(self)



