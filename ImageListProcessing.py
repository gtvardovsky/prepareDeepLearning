from PyQt5.QtCore import QObject, QDir, QFile
from CommonProcessingInterface import CommonProcessingInterface
from CommonState import COLOR_IMAGE
import cv2


class ImageListProcessing(CommonProcessingInterface):
    def __init__(self, sizeCutRegion):
        super().__init__(sizeCutRegion)
        self.m_image_list = []
        self.m_id_image = 0
        self.m_classificationFile = QFile()
        m_size_cutRegion = {}


    def set_WorkPath_Or_File(self, path):
        directory = QDir(path)
        if self.m_classificationFile.isOpen():
            self.m_classificationFile.close()
        self.m_path = path
        self.m_image_list.clear()
        self.m_id_image = 0
        self.getImagesList(directory.absolutePath());

    def getImagesList(self, dir):
        dir = QDir(dir)
        self.m_image_list = dir.entryList(["*.jpg, *.JPG, *.bmp, *.BMP, *.png, *.PNG, *.jpeg, *.JPEG"], QDir.Files)
        if self.m_image_list.count() > 0:
            self.openImage(self.m_id_image)

    def openImage(self, id):
        file = self.m_path + '/' + self.m_image_list[id]
        if self.m_color == COLOR_IMAGE['COLOR']:
            self.m_currentImage = cv2.imread(str(file), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        else:
            self.m_currentImage = cv2.imread(str(file), cv2.CV_LOAD_IMAGE_COLOR)
            if self.m_currentImage.channels == 1:
                cv2.cvtColor(self.m_currentImage, self.m_currentImage, cv2.CV_GRAY2RGB)
            else:
                cv2.cvtColor(self.m_currentImage, self.m_currentImage, cv2.CV_BGR2RGB)
        if self.m_currentImage.data:
            # Plugin Manager
            # emit newFrame(self.m_currentImage)






    # def cut_Regions_On_Image(self, items):
    #     if self.m_image_list.count() > 0:





