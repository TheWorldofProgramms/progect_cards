# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\testWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 70, 571, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.defLlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.defLlabel.setObjectName("defLlabel")
        self.gridLayout.addWidget(self.defLlabel, 1, 0, 1, 1)
        self.valueLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.valueLine.setObjectName("valueLine")
        self.gridLayout.addWidget(self.valueLine, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(400, 230, 231, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setStyleSheet("color:rgb(58, 176, 32);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setStyleSheet("color:rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.rightAnswerLcd = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.rightAnswerLcd.setObjectName("rightAnswerLcd")
        self.gridLayout_2.addWidget(self.rightAnswerLcd, 0, 1, 1, 1)
        self.answerLCD = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.answerLCD.setObjectName("answerLCD")
        self.gridLayout_2.addWidget(self.answerLCD, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 230, 160, 111))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка знаний"))
        self.defLlabel.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Значение:"))
        self.label.setText(_translate("MainWindow", "Определение:"))
        self.label_4.setText(_translate("MainWindow", "Количество правильных ответов:"))
        self.label_5.setText(_translate("MainWindow", "Количество ответов:"))
        self.nextWordButton.setText(_translate("MainWindow", "Следующее слово"))
        self.endButton.setText(_translate("MainWindow", "Закончить"))
