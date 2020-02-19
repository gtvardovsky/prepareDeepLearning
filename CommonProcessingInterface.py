from PyQt5.QtCore import QObject, QDir
from PyQt5.QtCore import QFile, QTextStream
import cv2
from CommonState import COLOR_IMAGE

class CommonProcessingInterface(QObject):
    def __init__(self, sizeCutRegion):
        super().__init__()
        self.saveFolderName = "Prepare Data"
        self.saveClassificationFileName = "classification.pd"
        self.saveTrainFolderName = "train"
        self.saveNegativeFolderName = "negative"
        self.saveTestFolderName = "test"
        self.m_savePath = ""
        self.m_trainSavePath = ""
        self.m_negativeSavePath = ""
        self.m_testSavePath = ""
        self.m_path = ""
        self.m_amountTrainCutImage = 0
        self.m_amountNegativeCutImage = 0
        self.m_amountTestCutImage = 0
        self.m_classificationTestFile = QFile()
        self.m_classificationNegativeFile = QFile()
        self.m_classificationTrainFile = QFile()
        self.m_size_CutRegion = {}
        self.m_color = COLOR_IMAGE['COLOR']
        self.m_check_Draw = False
        self.m_size_CutRegion = sizeCutRegion
        self.m_currentImage = None
        self.m_id_image = 0

    def set_Save_Path(self, path):
        self.m_savePath = path

    def cut_Regions_On_Image(self, items):
        if not self.m_save_Path:
            self.m_savePath = self.m_path + '/' + self.saveFolderName
            self.create_Folder(self.m_savePath)

            self.m_trainSavePath = self.m_savePath + '/' + self.saveTrainFolderName
            self.create_Folder(self.m_trainSavePath)

            self.m_negativeSavePath = self.m_savePath + "/" + self.saveNegativeFolderName;
            self.createFolder(self.m_negativeSavePath);

            self.m_testSavePath = self.m_savePath + "/" + self.saveTestFolderName;
            self.createFolder(self.m_testSavePath);
        self.createClassificationFile();
        for i in len(items):
            imageSave = ''
            test = items[i].getSaveFolderPath()
            out = QTextStream()
            if test == 'TRAIN':
                imageSave = self.m_trainSavePath + "/" + int(self.m_amountTrainCutImage) + ".png"
                out.setDevice(self.m_classificationTrainFile)
                count = self.m_amountTrainCutImage
            elif test == 'NEGATIVE':
                imageSave = self.m_negativeSavePath + "/" + int(self.m_amountNegativeCutImage) + ".png"
                out.setDevice(self.m_classificationNegativeFile)
                count = self.m_amountNegativeCutImage
            elif test == "TEST":
                imageSave = self.m_testSavePath + "/" + int(self.m_amountTestCutImage) + ".png"
                out.setDevice(self.m_classificationTestFile)
                count = self.m_amountTestCutImage
            image_roi = self.m_currentImage.clone()(items[i].region())
            width = self.m_sizeCutRegion.first
            height = self.m_sizeCutRegion.second
            cv2.resize(image_roi, width, height)
            if image_roi.channels() == 3:
                cv2.cvtColor(image_roi, image_roi, cv2.CV_BGR2RGB)
            cv2.imwrite(imageSave, image_roi)

            classificationData = ''
            for str in items[i].classificationList():
                classificationData += (str + " ")

            # pos = classificationData.lastIndexOf(QChar(' '));
            # asd

    def setColor(self, color):
        self.m_color = color
        self.openImage(self.m_id_image)

    def openImage(self, id):
        pass
