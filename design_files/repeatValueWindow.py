# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\repeatValueWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepeatValueWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 400)
        mainWindow.setMaximumSize(QtCore.QSize(700, 400))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 90, 541, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.defButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.defButton.setObjectName("defButton")
        self.gridLayout.addWidget(self.defButton, 1, 0, 1, 1)
        self.valueText = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.valueText.setUndoRedoEnabled(False)
        self.valueText.setReadOnly(True)
        self.valueText.setObjectName("valueText")
        self.gridLayout.addWidget(self.valueText, 1, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(420, 270, 211, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.repeatWordLcd = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.repeatWordLcd.setObjectName("repeatWordLcd")
        self.horizontalLayout.addWidget(self.repeatWordLcd)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 250, 160, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nextWordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.nextWordButton.setObjectName("nextWordButton")
        self.verticalLayout.addWidget(self.nextWordButton)
        self.endButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.endButton.setObjectName("endButton")
        self.verticalLayout.addWidget(self.endButton)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Повторение материала"))
        self.label.setText(_translate("mainWindow", "Определение:"))
        self.label_2.setText(_translate("mainWindow", "Значение:"))
        self.defButton.setText(_translate("mainWindow", "-"))
        self.label_3.setText(_translate("mainWindow", "Количество слов:"))
        self.nextWordButton.setText(_translate("mainWindow", "Следующее слово"))
        self.endButton.setText(_translate("mainWindow", "Закончить"))

