from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Main_window import Ui_MainWindow
from datebase import *

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.setFixedSize(1144, 829)  # Установка фиксированного размера окна
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 551, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 200, 651, 421))
        self.horizontalLayoutWidget.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.VhodButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.VhodButton.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.VhodButton.setFont(font)
        self.VhodButton.setIcon(QtGui.QIcon("Pictures/Enter.png"))  # Установка изображения для кнопки
        self.VhodButton.setIconSize(QtCore.QSize(350, 100))  # Задаем размер иконки
        self.VhodButton.setObjectName("VhodButton")
        self.horizontalLayout.addWidget(self.VhodButton)
        self.VhodButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # Устанавливаем стиль кнопки, чтобы текст был под иконкой
        self.VhodButton.setText("Вход")  # Добавляем пояснительную надпись

        self.pushButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setIcon(QtGui.QIcon("Pictures/Reg.png"))  # Установка изображения для кнопки
        self.pushButton.setIconSize(QtCore.QSize(350, 100))  # Задаем размер иконки
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # Устанавливаем стиль кнопки, чтобы текст был под иконкой
        self.pushButton.setText("Регистрация")  # Добавляем пояснительную надпись  # Добавляем пояснительную надпись
        self.horizontalLayout.addWidget(self.pushButton)

        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

        self.VhodButton.clicked.connect(lambda: self.openSecondWindow(FirstWindow))
        self.pushButton.clicked.connect(lambda: self.openThirdWindow(FirstWindow))

    def openThirdWindow(self, FirstWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegistrWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        FirstWindow.close()

    def openSecondWindow(self, FirstWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        FirstWindow.close()

    

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Кадровое агентство"))
        self.label.setText(_translate("FirstWindow", "Кадровое агентство"))
        self.VhodButton.setText(_translate("FirstWindow", "Вход"))
        self.pushButton.setText(_translate("FirstWindow", "Регистрация"))


class Ui_EnterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("EnterWindow")
        MainWindow.setFixedSize(1146, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 150, 502, 521))
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(500, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.VhodButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.VhodButton.setMinimumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.VhodButton.setFont(font)
        self.VhodButton.setObjectName("VhodButton")
        self.verticalLayout.addWidget(self.VhodButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.VhodButton.clicked.connect(lambda: self.openMainWindow(self.lineEdit.text(), self.lineEdit_2.text(),MainWindow))


        self.linkLabel = QtWidgets.QLabel(self.centralwidget) 
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linkLabel.setFont(font)
        self.linkLabel.setTextFormat(QtCore.Qt.AutoText)
        self.linkLabel.setOpenExternalLinks(False)
        self.linkLabel.setGeometry(QtCore.QRect(400, 650, 400, 50))
        self.linkLabel.setText("<a href='#'>Если нет аккаунта, зарегистрируйтесь</a>")
        self.linkLabel.linkActivated.connect(lambda: self.openRegWindow(MainWindow))

        self.lineEdit.setPlaceholderText("Логин")  # Добавить эту строку
        self.lineEdit_2.setPlaceholderText("Пароль")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openMainWindow(self, username, password, MainWindow):
        if username == "" or password == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка при входе")
            msg.setText("Необходимо заполнить все поля")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            try:
                cursor = connection.cursor()
                # Поиск пользователя в базе данных
                sql_query = "SELECT id_officer FROM users WHERE login = %s AND password = %s"
                data = (username, password)
                cursor.execute(sql_query, data)
                
                # Проверка результата запроса
                result = cursor.fetchone()
                if result:
                    id_officer = result['id_officer']
                    with open('account.txt', 'w') as file:  # Открытие файла в режиме записи
                        file.write(str(id_officer))  # Запись id_officer в файл
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Успешный вход")
                    msg.setText("Вход в систему выполнен успешно")
                    msg.addButton(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    self.MainWindow = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.MainWindow)  # Передача id_officer в следующее окно
                    self.MainWindow.show()
                    MainWindow.hide()

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Ошибка при входе")
                    msg.setText("Неверное имя пользователя или пароль")
                    msg.addButton(QtWidgets.QMessageBox.Ok)
                    msg.exec_()

            except pymysql.Error as e:
                # Обработка ошибок базы данных
                print("Произошла ошибка работы с базой данных:", e)


 
    def openRegWindow(self, MainWindow):
        # Метод для открытия формы Регист
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegistrWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход в систему"))
        self.label.setText(_translate("MainWindow", "Вход в систему"))
        self.VhodButton.setText(_translate("MainWindow", "Вход"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow","Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow","Пароль"))
        self.lineEdit.setToolTip(_translate("MainWindow","Логин"))
        self.lineEdit_2.setToolTip(_translate("MainWindow","Пароль"))


class Ui_RegistrWindow(object):
    def setupUi(self, RegistrWindow):
        RegistrWindow.setObjectName("RegistrWindow")
        RegistrWindow.setFixedSize(1144, 851)
        self.centralwidget = QtWidgets.QWidget(RegistrWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 0, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 110, 831, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 10, 609, 316))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(300, 100))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 360, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(22)

        self.linkLabel = QtWidgets.QLabel(self.centralwidget)  # Добавление QLabel к центральному виджету
        font = QtGui.QFont()
        font.setPointSize(13)
        self.linkLabel.setFont(font)
        self.linkLabel.setTextFormat(QtCore.Qt.AutoText)
        self.linkLabel.setOpenExternalLinks(False)
        self.linkLabel.setGeometry(QtCore.QRect(400, 650, 400, 50))  # Позиционирование QLabel
        self.linkLabel.setText("<a href='#'>Если есть аккаунт, войдите в систему</a>")

        self.linkLabel.linkActivated.connect(lambda: self.openLoginWindow(RegistrWindow))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        RegistrWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrWindow)

    

        self.pushButton.clicked.connect(lambda: self.handle_registration(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))

    def handle_registration(self, text1, text2, text3, text4, text5, text6):
        if text1 == "" or text2 == "" or text3 == "" or text4 == "" or text5 == "" or text6 == "":
            # Показать всплывающее окно с информацией о незаполненных полях
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка при регистрации")
            msg.setText("Необходимо заполнить все поля")
            ok_button = msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            # Показать всплывающее окно с информацией о успешной регистрации
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Успешная регистрация")
            msg.setText("Аккаунт успешно создан")
            ok_button = msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            # Создание SQL-запроса для внесения данных в таблицу "user"
            sql_query = "INSERT INTO users (surname, name, login, password, Telephone, Mail) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (text1, text2, text3, text4, text5, text6)

            # Выполнение SQL-запроса
            cursor = connection.cursor()
            cursor.execute(sql_query, data)
            connection.commit()

    def openLoginWindow(self, RegistrWindow):
        # Метод для открытия формы Вход в систему
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterWindow()  # Создание экземпляра класса Ui_MainWindow
        self.ui.setupUi(self.window)
        self.window.show()
        # Закрытие формы регистрации после открытия формы Вход в систему
        RegistrWindow.close()
        

    def retranslateUi(self, RegistrWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrWindow.setWindowTitle(_translate("RegistrWindow", "Регистрация в систему"))
        self.label.setText(_translate("RegistrWindow", "Регистрация"))
        self.pushButton.setText(_translate("RegistrWindow", "Зарегистрироваться"))
        self.lineEdit.setPlaceholderText(_translate("RegistrWindow", "Фамилия"))
        self.lineEdit_2.setPlaceholderText(_translate("RegistrWindow", "Имя"))
        self.lineEdit_3.setPlaceholderText(_translate("RegistrWindow", "Логин"))
        self.lineEdit_4.setPlaceholderText(_translate("RegistrWindow", "Пароль"))
        self.lineEdit_5.setPlaceholderText(_translate("RegistrWindow", "Почта"))
        self.lineEdit_6.setPlaceholderText(_translate("RegistrWindow", "Телефон"))

        self.lineEdit.setToolTip(_translate("RegistrWindow", "Фамилия"))
        self.lineEdit_2.setToolTip(_translate("RegistrWindow", "Имя"))
        self.lineEdit_3.setToolTip(_translate("RegistrWindow", "Логин"))
        self.lineEdit_4.setToolTip(_translate("RegistrWindow", "Пароль"))
        self.lineEdit_5.setToolTip(_translate("RegistrWindow", "Почта"))
        self.lineEdit_6.setToolTip(_translate("RegistrWindow", "Телефон"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
