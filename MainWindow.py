import sys
from os.path import expanduser
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QAction, QGraphicsRectItem, QFileDialog
from PyQt5.QtGui import QIcon, QBrush, QPen
from UI import mainwindow_ui
from ConstSettingWidget import ConstSettingsWidget
from Scene import Scene
from NewRectangle import newRectangle

class MainWindow(QMainWindow, mainwindow_ui.Ui_MainWindow):
    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле mainwindow_ui.py
        super().__init__()
        # Инициализация дизайна
        self.init_UI()


    def init_UI(self):
        self.setupUi(self)
        # Создаем экз класса ConstSettingsWidget, добавляем его на layout. layout в свою очередь добавляем на MainWindow
        mSetWid = ConstSettingsWidget()
        h_box = QHBoxLayout()
        h_box.addWidget(mSetWid)
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

        self.scene = Scene()
        # initRect = QRectF(0, 0, 60, 40)
        # rect = newRectangle(initRect)
        # scene.addItem(rect)
        self.graphicsView.setScene(self.scene)

    def open_file(self):
        dir = QFileDialog.getExistingDirectory(self, 'Open Directory',expanduser("~"),QFileDialog.ShowDirsOnly)
        print(dir)

    def addRect(self, checked):
        if self.scene.width() > 0 and self.scene.height() > 0:
            self.scene.set_draw_enable(checked)










def main():
    # Новый экз класса QApplication, экз класса MainWindow и показываем MainWindow
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()