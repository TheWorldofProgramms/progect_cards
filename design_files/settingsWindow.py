# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 160, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.exitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 3, 0, 1, 1)
        self.deleteAccountButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deleteAccountButton.setObjectName("deleteAccountButton")
        self.gridLayout.addWidget(self.deleteAccountButton, 1, 0, 1, 1)
        self.modeGameBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.modeGameBox.setEditable(False)
        self.modeGameBox.setObjectName("modeGameBox")
        self.modeGameBox.addItem("")
        self.modeGameBox.addItem("")
        self.gridLayout.addWidget(self.modeGameBox, 0, 0, 1, 1)
        self.menuButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.menuButton.setObjectName("menuButton")
        self.gridLayout.addWidget(self.menuButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 101, 20))
        self.label.setStyleSheet("*{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Настройки"))
        self.exitButton.setText(_translate("MainWindow", "Выйти"))
        self.deleteAccountButton.setText(_translate("MainWindow", "Удалить аккаунт"))
        self.modeGameBox.setItemText(0, _translate("MainWindow", "Проверка знаний"))
        self.modeGameBox.setItemText(1, _translate("MainWindow", "Повторение материала"))
        self.menuButton.setText(_translate("MainWindow", "Меню"))
        self.label.setText(_translate("MainWindow", "Режим игры:"))


