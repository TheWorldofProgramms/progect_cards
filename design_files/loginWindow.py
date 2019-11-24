# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 574)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 120, 160, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginLine.setText("")
        self.loginLine.setObjectName("loginLine")
        self.verticalLayout.addWidget(self.loginLine)
        self.passwordLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordLine.setObjectName("passwordLine")
        self.verticalLayout.addWidget(self.passwordLine)
        self.enterButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.enterButton.setObjectName("enterButton")
        self.verticalLayout.addWidget(self.enterButton)
        self.registrButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registrButton.setObjectName("registrButton")
        self.verticalLayout.addWidget(self.registrButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 381, 361))
        self.label.setMaximumSize(QtCore.QSize(400, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui_files\\../design_files/Cards.jpg"))
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Окно входа"))
        self.loginLine.setPlaceholderText(_translate("LoginWindow", "Введите Ваш логин"))
        self.passwordLine.setPlaceholderText(_translate("LoginWindow", "Введите Ваш пароль"))
        self.enterButton.setText(_translate("LoginWindow", "Войти"))
        self.registrButton.setText(_translate("LoginWindow", "Регистрация"))
