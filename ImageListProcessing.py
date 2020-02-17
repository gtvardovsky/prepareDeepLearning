from PyQt5.QtCore import *
from CommonProcessingInterface import CommonProcessingInterface
from CommonState import COLOR_IMAGE
from PyQt5.QtGui import *
import cv2


class ImageListProcessing(CommonProcessingInterface):
    newFrameSignal = pyqtSignal(object)
    def __init__(self, sizeCutRegion):
        super().__init__(sizeCutRegion)
        self.m_image_list = []
        self.m_id_image = 0
        self.m_classificationFile = QFile()
        m_size_cutRegion = {}
        #self.



    def setWorkPathOrFile(self, path):
        directory = QDir(path)
        if self.m_classificationFile.isOpen():
            self.m_classificationFile.close()
        self.m_path = path
        self.m_image_list.clear()
        self.m_id_image = 0
        self.getImagesList(directory.absolutePath());

    def getImagesList(self, dir):
        dir = QDir(dir)
        self.m_image_list = dir.entryList(["*.jpg"])
        if len(self.m_image_list) > 0:
            self.openImage(self.m_id_image)

    def openImage(self, id):
        file = self.m_path + '/' + self.m_image_list[id]
        if self.m_color == COLOR_IMAGE['COLOR']:
            self.m_currentImage = cv2.imread(str(file), cv2.IMREAD_GRAYSCALE)
        else:
            self.m_currentImage = cv2.imread(str(file), cv2.IMREAD_COLOR)
            if self.m_currentImage.channels == 1:
                cv2.cvtColor(self.m_currentImage, self.m_currentImage, cv2.CV_GRAY2RGB)
            else:
                cv2.cvtColor(self.m_currentImage, self.m_currentImage, cv2.CV_BGR2RGB)
        print(self.m_currentImage)
        if self.m_currentImage.data:
            # Plugin Manager
            self.newFrameSignal.emit(self.m_currentImage)
            pass






    # def cut_Regions_On_Image(self, items):
    #     if self.m_image_list.count() > 0:





