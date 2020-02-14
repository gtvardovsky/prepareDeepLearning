# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\George\Desktop\WelcomeToHell\imageslistwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_imagesListWidget(object):
    def setupUi(self, imagesListWidget):
        imagesListWidget.setObjectName("imagesListWidget")
        imagesListWidget.resize(300, 200)
        imagesListWidget.setMinimumSize(QtCore.QSize(0, 200))
        imagesListWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(imagesListWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(imagesListWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousImage_b = QtWidgets.QPushButton(self.groupBox)
        self.previousImage_b.setObjectName("previousImage_b")
        self.horizontalLayout.addWidget(self.previousImage_b)
        self.nextImage_b = QtWidgets.QPushButton(self.groupBox)
        self.nextImage_b.setObjectName("nextImage_b")
        self.horizontalLayout.addWidget(self.nextImage_b)
        self.cutImage_b = QtWidgets.QPushButton(self.groupBox)
        self.cutImage_b.setObjectName("cutImage_b")
        self.horizontalLayout.addWidget(self.cutImage_b)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.plugin_cb = QtWidgets.QComboBox(self.groupBox)
        self.plugin_cb.setEnabled(True)
        self.plugin_cb.setObjectName("plugin_cb")
        self.horizontalLayout_2.addWidget(self.plugin_cb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.color_b = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_b.sizePolicy().hasHeightForWidth())
        self.color_b.setSizePolicy(sizePolicy)
        self.color_b.setCheckable(True)
        self.color_b.setChecked(True)
        self.color_b.setObjectName("color_b")
        self.verticalLayout.addWidget(self.color_b)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(imagesListWidget)
        QtCore.QMetaObject.connectSlotsByName(imagesListWidget)

    def retranslateUi(self, imagesListWidget):
        _translate = QtCore.QCoreApplication.translate
        imagesListWidget.setWindowTitle(_translate("imagesListWidget", "Form"))
        self.groupBox.setTitle(_translate("imagesListWidget", "Работа с каталогом изображений"))
        self.previousImage_b.setText(_translate("imagesListWidget", "<<"))
        self.nextImage_b.setText(_translate("imagesListWidget", ">>"))
        self.cutImage_b.setText(_translate("imagesListWidget", "Cut"))
        self.label.setText(_translate("imagesListWidget", " Plugin"))
        self.color_b.setText(_translate("imagesListWidget", "Color"))
