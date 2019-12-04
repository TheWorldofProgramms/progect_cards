# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\statisticWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticWindow(object):
    def setupUi(self, StatisticWindow):
        StatisticWindow.setObjectName("StatisticWindow")
        StatisticWindow.resize(600, 600)
        StatisticWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(StatisticWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 90, 281, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.precentLcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.precentLcd.setObjectName("precentLcd")
        self.gridLayout.addWidget(self.precentLcd, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.repeatWordsLcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.repeatWordsLcd.setObjectName("repeatWordsLcd")
        self.gridLayout.addWidget(self.repeatWordsLcd, 3, 1, 1, 1)
        self.answerWordLcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.answerWordLcd.setObjectName("answerWordLcd")
        self.gridLayout.addWidget(self.answerWordLcd, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rightAnswerLcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.rightAnswerLcd.setObjectName("rightAnswerLcd")
        self.gridLayout.addWidget(self.rightAnswerLcd, 0, 1, 1, 1)
        self.menuButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.menuButton.setObjectName("menuButton")
        self.gridLayout.addWidget(self.menuButton, 4, 0, 1, 2)
        StatisticWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(StatisticWindow)
        self.toolBar.setObjectName("toolBar")
        StatisticWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(StatisticWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_files\\../design_files/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(StatisticWindow)
        self.actionExit.triggered.connect(StatisticWindow.close)
        QtCore.QMetaObject.connectSlotsByName(StatisticWindow)

    def retranslateUi(self, StatisticWindow):
        _translate = QtCore.QCoreApplication.translate
        StatisticWindow.setWindowTitle(_translate("StatisticWindow", "Статистика"))
        self.label_4.setText(_translate("StatisticWindow", "Процент верности:"))
        self.label_3.setText(_translate("StatisticWindow", "Слов повторено:"))
        self.label_2.setText(_translate("StatisticWindow", "Ответов дано:"))
        self.label.setText(_translate("StatisticWindow", "Правильных ответов дано:"))
        self.menuButton.setText(_translate("StatisticWindow", "Меню"))
        self.toolBar.setWindowTitle(_translate("StatisticWindow", "toolBar"))
        self.actionExit.setText(_translate("StatisticWindow", "Exit"))
        self.actionExit.setToolTip(_translate("StatisticWindow", "Exit window"))

