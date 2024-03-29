# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\cardsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardsWindow(object):
    def setupUi(self, CardsWindow):
        CardsWindow.setObjectName("CardsWindow")
        CardsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CardsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 430, 601, 83))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.modulsLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.modulsLine.setObjectName("modulsLine")
        self.gridLayout.addWidget(self.modulsLine, 0, 0, 1, 1)
        self.editButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 0, 1, 1, 1)
        self.playButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.playButton.setObjectName("playButton")
        self.gridLayout.addWidget(self.playButton, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.modulsLabel = QtWidgets.QLabel(self.centralwidget)
        self.modulsLabel.setGeometry(QtCore.QRect(80, 80, 47, 13))
        self.modulsLabel.setObjectName("modulsLabel")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 20, 601, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchLine = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.searchLine.setObjectName("searchLine")
        self.gridLayout_2.addWidget(self.searchLine, 0, 0, 1, 1)
        self.modulsTable = QtWidgets.QTableView(self.centralwidget)
        self.modulsTable.setGeometry(QtCore.QRect(80, 110, 600, 291))
        self.modulsTable.setMaximumSize(QtCore.QSize(600, 300))
        self.modulsTable.setObjectName("modulsTable")
        CardsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(CardsWindow)
        self.toolBar.setObjectName("toolBar")
        CardsWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSettings = QtWidgets.QAction(CardsWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("design_files/images/Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionStatistic = QtWidgets.QAction(CardsWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("design_files/images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatistic.setIcon(icon1)
        self.actionStatistic.setObjectName("actionStatistic")
        self.actionExit = QtWidgets.QAction(CardsWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("design_files//images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionStatistic)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(CardsWindow)
        self.actionExit.triggered.connect(CardsWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CardsWindow)

    def retranslateUi(self, CardsWindow):
        _translate = QtCore.QCoreApplication.translate
        CardsWindow.setWindowTitle(_translate("CardsWindow", "Карточки"))
        self.modulsLine.setPlaceholderText(_translate("CardsWindow", "Введите названия нужных модулей"))
        self.editButton.setText(_translate("CardsWindow", "Редактировать"))
        self.playButton.setText(_translate("CardsWindow", "Играть"))
        self.pushButton_3.setText(_translate("CardsWindow", "Удалить"))
        self.modulsLabel.setText(_translate("CardsWindow", "Модули"))
        self.searchButton.setText(_translate("CardsWindow", "Найти"))
        self.searchLine.setPlaceholderText(_translate("CardsWindow", "Введите название модуля для поиска"))
        self.toolBar.setWindowTitle(_translate("CardsWindow", "toolBar"))
        self.actionSettings.setText(_translate("CardsWindow", "Settings"))
        self.actionSettings.setToolTip(_translate("CardsWindow", "Settings open"))
        self.actionStatistic.setText(_translate("CardsWindow", "Statistic"))
        self.actionStatistic.setToolTip(_translate("CardsWindow", "Statistic open"))
        self.actionExit.setText(_translate("CardsWindow", "Exit"))
        self.actionExit.setToolTip(_translate("CardsWindow", "Exit window"))


