from PyQt5 import QtCore, QtGui, QtWidgets
from datebase import *

class Ui_About_kadrovik(object):
    def setupUi(self, About_kadrovik):
        About_kadrovik.setObjectName("About_kadrovik")
        About_kadrovik.resize(725, 500)
        About_kadrovik.setMinimumSize(QtCore.QSize(725, 500))
        About_kadrovik.setMaximumSize(QtCore.QSize(725, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About_kadrovik.setWindowIcon(icon)
        self.Zagolovok = QtWidgets.QLabel(About_kadrovik)
        self.Zagolovok.setGeometry(QtCore.QRect(140, 0, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Zagolovok.setFont(font)
        self.Zagolovok.setObjectName("Zagolovok")
        self.formLayoutWidget = QtWidgets.QWidget(About_kadrovik)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 100, 591, 276))
        self.formLayoutWidget.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.SaveButton = QtWidgets.QPushButton(About_kadrovik)
        self.SaveButton.setGeometry(QtCore.QRect(200, 400, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SaveButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveButton.setIcon(icon1)
        self.SaveButton.setObjectName("SaveButton")
        self.ExitButton = QtWidgets.QPushButton(About_kadrovik)
        self.ExitButton.setGeometry(QtCore.QRect(630, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon2)
        self.ExitButton.setObjectName("ExitButton")

        self.retranslateUi(About_kadrovik)
        QtCore.QMetaObject.connectSlotsByName(About_kadrovik)

        # Получение курсора для взаимодействия с базой данных
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        with open('account.txt', 'r') as file:  # Открытие файла в режиме чтения
            id_officer = file.read()  # Чтение id_officer из файла
        sql_query = "SELECT * FROM users WHERE id_officer = %s"
        cursor.execute(sql_query, (id_officer,))
        user_data = cursor.fetchone()

        # Заполнение полей формы информацией о пользователе
        if user_data:
            self.lineEdit_2.setText(user_data['name'])
            self.lineEdit.setText(user_data['surname'])
            self.lineEdit_3.setText(user_data['mail'])
            self.lineEdit_4.setText(str(user_data['telephone']))

        self.SaveButton.clicked.connect(lambda: self.save_changes(id_officer, cursor))
        self.ExitButton.clicked.connect(About_kadrovik.close)

    def retranslateUi(self, About_kadrovik):
        _translate = QtCore.QCoreApplication.translate
        About_kadrovik.setWindowTitle(_translate("About_kadrovik", "Сведения о кадровике"))
        self.Zagolovok.setText(_translate("About_kadrovik", "Сведения о кадровике"))
        self.label_2.setText(_translate("About_kadrovik", "Имя"))
        self.label_3.setText(_translate("About_kadrovik", "Почта"))
        self.label_4.setText(_translate("About_kadrovik", "Телефон"))
        self.label.setText(_translate("About_kadrovik", "Фамилия"))
        self.SaveButton.setText(_translate("About_kadrovik", "Сохранить изменения"))
        self.ExitButton.setText(_translate("About_kadrovik", "Назад"))

    def save_changes(self, user_id, cursor):
        # Получение новых данных из полей формы
        new_name = self.lineEdit.text()
        new_surname = self.lineEdit_2.text()
        new_email = self.lineEdit_3.text()
        new_phone = self.lineEdit_4.text()

        # Удалить следующую строку
        # cursor = connection.cursor()

        sql_query = "UPDATE users SET name = %s, surname = %s, Mail = %s, Telephone = %s WHERE id_officer = %s"
        cursor.execute(sql_query, (new_name, new_surname, new_email, new_phone, user_id))
        connection.commit()

        # Оповещение об успешном сохранении изменений
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Сохранить изменения")
        msg.setText("Данные успешно сохранены.")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About_kadrovik = QtWidgets.QDialog()
    ui = Ui_About_kadrovik()
    ui.setupUi(About_kadrovik)
    About_kadrovik.show()
    sys.exit(app.exec_())
