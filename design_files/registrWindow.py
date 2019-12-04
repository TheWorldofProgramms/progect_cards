# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\registrWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistrWindow(object):
    def setupUi(self, RegistrWindow):
        RegistrWindow.setObjectName("RegistrWindow")
        RegistrWindow.resize(794, 600)
        self.centralwidget = QtWidgets.QWidget(RegistrWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 70, 226, 414))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginLine.setObjectName("loginLine")
        self.verticalLayout.addWidget(self.loginLine)
        self.passwordLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordLine.setObjectName("passwordLine")
        self.verticalLayout.addWidget(self.passwordLine)
        self.passwordLine2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordLine2.setObjectName("passwordLine2")
        self.verticalLayout.addWidget(self.passwordLine2)
        self.wordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.wordLabel.setMaximumSize(QtCore.QSize(250, 16777215))
        self.wordLabel.setStyleSheet("<p> Введите специальное слово, </p>\n"
"<p> которое будет использоваться </p>\n"
"<p> для востановления пароля. </p>")
        self.wordLabel.setWordWrap(True)
        self.wordLabel.setObjectName("wordLabel")
        self.verticalLayout.addWidget(self.wordLabel)
        self.wordLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.wordLine.setObjectName("wordLine")
        self.verticalLayout.addWidget(self.wordLine)
        self.registrButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registrButton.setObjectName("registrButton")
        self.verticalLayout.addWidget(self.registrButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 400, 400))
        self.label.setMaximumSize(QtCore.QSize(400, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("design_files/images/brain.png"))
        self.label.setObjectName("label")
        RegistrWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegistrWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrWindow)
        RegistrWindow.setTabOrder(self.passwordLine, self.passwordLine2)
        RegistrWindow.setTabOrder(self.passwordLine2, self.loginLine)
        RegistrWindow.setTabOrder(self.loginLine, self.wordLine)
        RegistrWindow.setTabOrder(self.wordLine, self.registrButton)

    def retranslateUi(self, RegistrWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrWindow.setWindowTitle(_translate("RegistrWindow", "Окно регистрации"))
        self.loginLine.setPlaceholderText(_translate("RegistrWindow", "Логин"))
        self.passwordLine.setPlaceholderText(_translate("RegistrWindow", "Пароль"))
        self.passwordLine2.setPlaceholderText(_translate("RegistrWindow", "Повторите пароль"))
        self.wordLabel.setText(_translate("RegistrWindow", "Введите специальное слово, которое будет испоьзоваться для востановления пароля:"))
        self.wordLine.setPlaceholderText(_translate("RegistrWindow", "Ваше слово"))
        self.registrButton.setText(_translate("RegistrWindow", "Зарегистрироваться"))
