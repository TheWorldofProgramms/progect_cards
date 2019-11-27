# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\menuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMaximumSize(QtCore.QSize(600, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 130, 241, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cardsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cardsButton.setObjectName("cardsButton")
        self.verticalLayout.addWidget(self.cardsButton)
        self.statisticButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.statisticButton.setObjectName("statisticButton")
        self.verticalLayout.addWidget(self.statisticButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.helpButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.menuLabel = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel.setGeometry(QtCore.QRect(230, 80, 111, 51))
        self.menuLabel.setStyleSheet("*{\n"
"font: 75 30pt \"MS Sans Serif\";\n"
"text-decoration: underline;\n"
"}")
        self.menuLabel.setObjectName("menuLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.cardsButton.setText(_translate("MainWindow", "Карточки"))
        self.statisticButton.setText(_translate("MainWindow", "Статистика"))
        self.settingsButton.setText(_translate("MainWindow", "Настройки"))
        self.helpButton.setText(_translate("MainWindow", "Помощь"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.menuLabel.setText(_translate("MainWindow", "Меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())