from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget
from CommonStateAndData import WORK_STATE
from ImagesListWidget import ImagesListWidget

class ImageProcessingManager(QObject):
    def __init__(self):
        self.m_current_state = WORK_STATE.IMAGES_LIST.name
        self.m_base_widget = QWidget()


    def get_current_widget(self, state):
        if state == WORK_STATE.IMAGES_LIST.name:
            widget = ImagesListWidget




