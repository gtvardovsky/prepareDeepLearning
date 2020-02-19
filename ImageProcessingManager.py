from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget
from ImagesListWidget import ImagesListWidget
from ImageListProcessing import ImageListProcessing
from CommonState import WORK_STATE

class ImageProcessingManager(QObject):
    def __init__(self):
        super().__init__()
        self.m_current_state = 'IMAGES_LIST'
        self.m_base_widget = QWidget()
        self.m_processingLevel = {}
        self.m_sizeCutRegion = (256, 256)
        # self.m_processingLevel[WORK_STATE['VIDEO']] = VideoProcessing()
        self.m_processingLevel[WORK_STATE['IMAGES_LIST']] = ImageListProcessing(self.m_sizeCutRegion)

        #self.m_processingLevel[WORK_STATE['IMAGES_LIST']].newFrameSignal.connect(self.slot)



    def get_current_widget(self, state):
        if self.m_base_widget is not None:
            del self.m_base_widget
            self.m_base_widget = None
        if state == WORK_STATE['IMAGES_LIST']:
            widget = ImagesListWidget(self.m_processingLevel[state])
            # connect
            self.m_base_widget = widget
        elif state == WORK_STATE['VIDEO']:
            # pass
            pass
        else :
            pass
        self.m_current_state = state
        return self.m_base_widget

    def setWorkPathOrFile(self, path):
        self.m_processingLevel[self.m_current_state].setWorkPathOrFile(path)

    def slot(self, img):
        print(img)





