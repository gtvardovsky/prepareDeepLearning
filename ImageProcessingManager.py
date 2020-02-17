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
        if state == WORK_STATE['IMAGES_LIST']:
            widget = ImagesListWidget()
            # connect
            self.m_base_widget = widget
        elif state == WORK_STATE['VIDEO']:
            # pass
            pass
        else :
            pass

    def setWorkPathOrFile(self, path):
        a = self.m_processingLevel[self.m_current_state]
        # self.m_processingLevel[self.m_current_state].setWorkPathOrFile(path)
        a.setWorkPathOrFile(path)

    def slot(self, img):
        print(img)





