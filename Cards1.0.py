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


#Сделанно(нужна проверка)
class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.window_reg = RegistrWindow()
        self.window_reg.show()

        #Нажимается кнопка "Войти"
        self.enterButton.clicked.connect(self.enter)
        #Нажимается кнопка "Регистрация"
        self.registrButton.clicked.connect(self.registr)

    def enter(self): #Вход в личный кабинет
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
            self.window_menu = MenuWindow()
            self.window_menu.show()
            self.close()

        self.window_menu = MenuWindow()
        self.window_menu.show()
        self.close()

    def registr(self): #Открыть окно создания нового аккаунта
        self.window_reg = RegistrWindow()
        self.window_reg.show()


#Редактирование!!!
class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.id_user = args[0]
        #self.word_user = args[1]

        #Нажата кнопка "Карточки"
        self.cardsButton.clicked.connect(self.cards)

        #Нажата кнопак "Статистика"
        self.statisticButton.clicked.connect(self.statistic)

        #Нажата кнопка "Настройки"
        self.settingsButton.clicked.connect(self.settings)

        #Нажата кнопка "Помощь"
        #self.helpButton.clicked.connect(self.help)

    def cards(self):
        self.window_cards = CardsWindow()
        self.window_cards.show()

    def statistic(self):
        self.window_statistic = StatisticWindow()
        self.window_statistic.show()

    def settings(self):
        self.window_settings = SettingsWindow()
        self.window_settings.show()


#Сделанно(нужна проверка) !!!Проблема с кнопкой регистрации!!!
class RegistrWindow(QWidget, Ui_RegistrWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        #Нажата кнопка "зарегистрироваться"
        self.registrButton.clicked.connect(self.registr1)

    def registr1(self): #Создание нового аккаунта
        #Получаем данные, введенные пользователем
        login, word = self.loginLine.text(), self.wordLine.text()
        password1, password2 = self.passwordLine.text(), self.passwordLine2.text()

        # Подключаемся к БД пользователей
        con = sqlite3.connect("BDUsers")
        cur = con.cursor()

        # Ищем в БД пользователей нужного человека
        results = cur.execute("""SELECT id FROM Users 
                            WHERE User_name = ?""",
                              (login, )).fetchone()

        # Проверяем данные
        try:
            len(results)
        except TypeError:
            if login == '' or word == '' or password1 == '' or password2 == '':
                messege = QMessageBox(self)
                messege.setWindowTitle("Сообщение об ошибке")
                messege.setText('Все поля должны быть заполнены')
                messege.show()
            if password1 == password2:# Проверяем совпадение введеных паролей
                # Вводим данные пользователя в БД
                cur.execute("""INSERT INTO Users (User_name, User_password, User_word) VALUES (?, ?, ?)""",
                            (login, password1, word))
                self.close()
            else:# Сообщение об ошибке
                messege = QMessageBox(self)
                messege.setWindowTitle("Сообщение об ошибке")
                messege.setText('Пароли не совпадают')
                messege.show()
        else:
            # Сообщаем, что данный логин занят
            messege = QMessageBox(self)
            messege.setWindowTitle("Сообщение об ошибке")
            messege.setText('Данный логин уже занят')
            messege.show()


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