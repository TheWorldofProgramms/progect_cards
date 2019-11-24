# -*- utf-8: -*-

from design_files.cardsWindow import Ui_CardsWindow
from design_files.editCardsWindow import Ui_EditCardsWindow
from design_files.loginWindow import Ui_LoginWindow
from design_files.menuWindow import Ui_MenuWindow
from design_files.registrWindow import Ui_RegistrWindow
from design_files.repeatValueWindow import Ui_RepeatValueWindow
from design_files.settingsWindow import Ui_SettingsWindow
from design_files.statisticWindow import Ui_StatisticWindow
from design_files.testWindow import Ui_TestWindow

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
import sqlite3



class CardsWindow(QMainWindow, Ui_CardsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class EditCardsWindow(QMainWindow, Ui_EditCardsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Нажимается кнопка "Войти"
        self.enterButton.clicked.connect(self.enter)
        #Нажимается кнопка "Регистрация"
        self.registrButton.clicked.connect(self.registr)

    def enter(self):
        #Считываем введеные логин и пароль
        login, password = self.loginLine.text(), self.passwordLine.text()

        #Подключаемся к БД пользователей
        con = sqlite3.connect("BDUsers")
        cur = con.cursor()

        #Ищем в БД пользователей нужного человека
        results = cur.execute("""SELECT id, User_word FROM Users 
                    WHERE User_name = ? AND User_password = ?""",
                              (login, password)).fetchone()

        #Проверяем данные
        try:
            len(results)
        except TypeError:
            # Выводим сообщение об ошибке
            messege = QMessageBox(self)
            messege.setWindowTitle("Сообщение об ошибке")
            messege.setText('Неправильно введен логин и/или пароль')
            messege.show()
        else:
            #Сохраняем id пользователя и создаем окно меню
            menu = MenuWindow(results)

    def registr(self):
        self.window_reg = QMainWindow()
        self.ui = Ui_RegistrWindow()
        self.ui.setupReg(self.window_reg)
        self.window_reg.show()


class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.id_user = args[0]
        self.word_user = args[1]


class RegistrWindow(QWidget, Ui_RegistrWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)


class RepeatValueWindow(QMainWindow, Ui_RepeatValueWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class StatisticWindow(QMainWindow, Ui_StatisticWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TestWindow(QMainWindow, Ui_TestWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec_())