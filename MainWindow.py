import sys
from os.path import expanduser
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QPen
from UI import mainwindow_ui
from ConstSettingWidget import ConstSettingsWidget
from Scene import Scene
from ImageProcessingManager import ImageProcessingManager
from ImagesListWidget import ImagesListWidget
from NewRectangle import newRectangle
from CommonState import WORK_STATE

class MainWindow(QMainWindow, mainwindow_ui.Ui_MainWindow):
    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле mainwindow_ui.py
        super().__init__()
        # Инициализация дизайна
        self.init_UI()
        self.mScene = Scene()
        self.m_imageProcessingManager = ImageProcessingManager()
        self.graphicsView.setScene(self.mScene)
        self.m_workState = WORK_STATE['IMAGES_LIST']
        self.m_pointWidget = self.m_imageProcessingManager.get_current_widget(self.m_workState)
        self.m_spacer = QSpacerItem(1,1,QSizePolicy.Expanding, QSizePolicy.Expanding)


    def init_UI(self):
        self.setupUi(self)
        # Создаем экз класса ConstSettingsWidget, добавляем его на layout. layout в свою очередь добавляем на MainWindow
        mSetWid = ConstSettingsWidget()
        mSetWid.mImageRadio.toggled.connect(lambda : self.setWorkStateImage(mSetWid.mImageRadio))
        mSetWid.mVideoRadio.toggled.connect(lambda :self.setWorkStateVideo(mSetWid.mVideo_radio))
        mSetWid.mWebCamRadio.toggled.connect(lambda :self.setWorkStateWebcam(mSetWid.mWebCam_radio))
        mImageWidget = ImagesListWidget()
        h_box = QHBoxLayout()
        h_box.addWidget(mSetWid)
        h_box.addWidget(mImageWidget)
        self.SettingsGroupBox.setLayout(h_box)

        # Добавление иконок в ToolBar
        open_icon = QIcon("icon/folder.png")
        open_action = QAction(open_icon, "Open file", self)
        self.mainToolBar.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        add_rectangle_icon = QIcon("icon/rect.png")
        add_rectangle_action = QAction(add_rectangle_icon, "New rectangle", self)
        add_rectangle_action.setCheckable(True)
        self.mainToolBar.addAction(add_rectangle_action)
        add_rectangle_action.triggered[bool].connect(self.addRect)

        delete_icon = QIcon("icon/delete.png")
        delete_action= QAction(delete_icon, "Del rectangle", self)
        self.mainToolBar.addAction(delete_action)

        save_icon = QIcon("icon/save.png")
        save_action = QAction(save_icon, "Cut rectangle", self)
        self.mainToolBar.addAction(save_action)

        self.mainToolBar.addSeparator()

        open_config_icon = QIcon("icon/settings.png")
        open_config_action = QAction(open_config_icon, "Open Configuration File", self)
        self.mainToolBar.addAction(open_config_action)

        open_config_widget_icon = QIcon("icon/config_settings.png")
        open_config_widget_action = QAction(open_config_widget_icon, "Open Widget Configuration Settings", self)
        self.mainToolBar.addAction(open_config_widget_action)

        open_plugin_widget_icon = QIcon("icon/widget.png")
        open_plugin_widget_action = QAction(open_plugin_widget_icon, "Open Widget Configuration Settings", self)
        self.mainToolBar.addAction(open_plugin_widget_action)

        #
        redBrush = QBrush(Qt.red)
        blackPen = QPen(Qt.black)
        blackPen.setWidth(2)


        # initRect = QRectF(0, 0, 60, 40)
        # rect = newRectangle(initRect)
        # self.scene.addItem(rect)

    def setWorkStateImage(self, checked):
        if checked:
            self.m_workState = WORK_STATE['IMAGES_LIST']
            self.setControlWidget(self.m_workState)
    def setWorkStateVideo(self, checked):
        if checked:
            self.m_workState = WORK_STATE['VIDEO']
            # self.setControlWidget(self.m_workState)

    def setWorkStateWebcam(self, checked):
        if checked:
            self.m_workState = WORK_STATE['WEBCAM']
            # self.setControlWidget(self.m_workState)

    def open_file(self):
        if self.m_workState == WORK_STATE['IMAGES_LIST']:
            dir = QFileDialog.getExistingDirectory(self, 'Open Directory',expanduser("~"),QFileDialog.ShowDirsOnly)
            if dir is not None:
                self.m_imageProcessingManager.setWorkPathOrFile(dir)

        elif self.m_workState == WORK_STATE['VIDEO']:
            dir = QFileDialog.getOpenFileName(self, 'Open File',expanduser("~"), "Video (*.mp4 *.mkv *.avi *.mpeg)")
            if dir is not None:
                self.m_imageProcessingManager.setWorkPathOrFile(dir)

        elif self.m_workState == WORK_STATE['WEBCAM']:
            pass


    def addRect(self, checked):
        if self.mScene.width() > 0 and self.mScene.height() > 0:
            self.mScene.set_draw_enable(checked)


    def setControlWidger(self, state):
        self.SettingsGroupBox.layout().removeWidget(self.m_pointWidget)
        self.SettingsGroupBox.layout().removeItem(self.m_spacer)
        self.m_pointWidget = self.m_imageProcessingManager.get_current_widget(state)
        if self.m_pointWidget is not None:
            self.mScene.clear()
            self.SettingsGroupBox.layout().addWidget(self.m_pointWidget)
            self.SettingsGroupBox.layout().addItem(self.m_spacer)


def main():
    # Новый экз класса QApplication, экз класса MainWindow и показываем MainWindow
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()