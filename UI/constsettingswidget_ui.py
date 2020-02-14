# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\George\Desktop\WelcomeToHell\constsettingswidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConstSettingsWidget(object):
    def setupUi(self, ConstSettingsWidget):
        ConstSettingsWidget.setObjectName("ConstSettingsWidget")
        ConstSettingsWidget.resize(175, 200)
        ConstSettingsWidget.setMinimumSize(QtCore.QSize(175, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(ConstSettingsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputChanged_gb = QtWidgets.QGroupBox(ConstSettingsWidget)
        self.inputChanged_gb.setObjectName("inputChanged_gb")
        self.verticalLayout.addWidget(self.inputChanged_gb)
        self.cutSizeSettings_gb = QtWidgets.QGroupBox(ConstSettingsWidget)
        self.cutSizeSettings_gb.setObjectName("cutSizeSettings_gb")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cutSizeSettings_gb)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.cutSizeSettings_gb)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.cutSizeSettings_gb)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.widthResizeValue_sb = QtWidgets.QSpinBox(self.cutSizeSettings_gb)
        self.widthResizeValue_sb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widthResizeValue_sb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthResizeValue_sb.setMinimum(7)
        self.widthResizeValue_sb.setMaximum(1024)
        self.widthResizeValue_sb.setProperty("value", 256)
        self.widthResizeValue_sb.setObjectName("widthResizeValue_sb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widthResizeValue_sb)
        self.heightResizeValue_sb = QtWidgets.QSpinBox(self.cutSizeSettings_gb)
        self.heightResizeValue_sb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.heightResizeValue_sb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightResizeValue_sb.setMinimum(7)
        self.heightResizeValue_sb.setMaximum(1024)
        self.heightResizeValue_sb.setProperty("value", 256)
        self.heightResizeValue_sb.setObjectName("heightResizeValue_sb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.heightResizeValue_sb)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.cutSizeSettings_gb)

        self.retranslateUi(ConstSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(ConstSettingsWidget)

    def retranslateUi(self, ConstSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        ConstSettingsWidget.setWindowTitle(_translate("ConstSettingsWidget", "Form"))
        self.inputChanged_gb.setTitle(_translate("ConstSettingsWidget", "Источник входных данных"))
        self.cutSizeSettings_gb.setTitle(_translate("ConstSettingsWidget", "Resize вырезаемой области"))
        self.label.setText(_translate("ConstSettingsWidget", "Ширина"))
        self.label_2.setText(_translate("ConstSettingsWidget", "Высота"))
