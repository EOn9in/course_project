from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from About_kadrovic import Ui_About_kadrovik
from datebase import *
import datetime
import os
from reportlab.lib import colors,fonts
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.showMaximized()  # Открыть окно на весь экран

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 350, 1330, 302))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Employer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_4.setShortcut("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Applicants.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Vac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 650, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(940, 650, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1420, 650, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 0, 101, 91))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/Info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1780, 10, 101, 91))
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Pictures/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Name_Form = QtWidgets.QLabel(self.centralwidget)
        self.Name_Form.setGeometry(QtCore.QRect(800, 0, 361, 97))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.Name_Form.setFont(font)
        self.Name_Form.setObjectName("Name_Form")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1810, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.show_exit_dialog)

        '''self.id_officer = id_officer'''
        self.pushButton.clicked.connect(lambda: self.openAboutWindow())

        self.pushButton_5.clicked.connect(lambda: self.openVacanciesForm(MainWindow))
        self.pushButton_4.clicked.connect(lambda: self.openEmployersForm(MainWindow))
        self.pushButton_3.clicked.connect(lambda: self.openApplicantsForm(MainWindow))

    def openVacanciesForm(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VacWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def openEmployersForm(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RabotWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def openApplicantsForm(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SoiscWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()


    def show_exit_dialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Выход из системы")
        msg.setText("Вы уверены, что хотите выйти из системы?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.No)
        reply = msg.exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()

    def exit_system(self, i):
        if i.text() == "Нет":
            QtWidgets.qApp.activeModalWidget().close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кадровое агентство"))
        self.label.setText(_translate("MainWindow", "Работодатели"))
        self.label_2.setText(_translate("MainWindow", "Соискатели"))
        self.label_3.setText(_translate("MainWindow", "Вакансии"))
        self.Name_Form.setText(_translate("MainWindow", "Кадровик"))
        self.label_4.setText(_translate("MainWindow", "Сведения о кадровике"))
        self.label_5.setText(_translate("MainWindow", "Выход"))


    def openAboutWindow(self):
        # Метод для открытия формы Вход в систему
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_About_kadrovik()
        self.ui.setupUi(self.window)  # Передача user_id в метод setupUi
        self.window.show()


class Ui_VacWindow(object):
    def setupUi(self, VacWindow):
        VacWindow.setObjectName("VacWindow")
        VacWindow.setWindowModality(QtCore.Qt.NonModal)
        VacWindow.setEnabled(True)
        VacWindow.showMaximized()  # Открыть окно на весь экран

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VacWindow.sizePolicy().hasHeightForWidth())
        VacWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VacWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(VacWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(790, 0, 451, 51))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_nameWindow = QtWidgets.QLabel(self.frame)
        self.label_nameWindow.setGeometry(QtCore.QRect(140, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_nameWindow.setFont(font)
        self.label_nameWindow.setObjectName("label_nameWindow")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1820, 0, 91, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.NewVacButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewVacButton.setGeometry(QtCore.QRect(10, 80, 71, 51))
        self.NewVacButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewVacButton.setIcon(icon2)
        self.NewVacButton.setIconSize(QtCore.QSize(50, 50))
        self.NewVacButton.setObjectName("NewVacButton")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(90, 80, 71, 51))
        self.EditButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditButton.setIcon(icon3)
        self.EditButton.setIconSize(QtCore.QSize(50, 50))
        self.EditButton.setObjectName("EditButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(170, 80, 71, 51))
        self.DeleteButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon4)
        self.DeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.DeleteButton.setObjectName("DeleteButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(250, 80, 71, 51))
        self.SearchButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Pictures/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon5)
        self.SearchButton.setIconSize(QtCore.QSize(50, 50))
        self.SearchButton.setObjectName("SearchButton")
        self.tableVac = QtWidgets.QTableView(self.centralwidget)
        self.tableVac.setGeometry(QtCore.QRect(10, 180, 741, 831))
        self.tableVac.setObjectName("tableVac")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 741, 31))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_nameWindow_2 = QtWidgets.QLabel(self.frame_2)
        self.label_nameWindow_2.setGeometry(QtCore.QRect(310, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_2.setFont(font)
        self.label_nameWindow_2.setObjectName("label_nameWindow_2")
        self.DeleteButton_Candidate = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton_Candidate.setGeometry(QtCore.QRect(1440, 90, 71, 51))
        self.DeleteButton_Candidate.setText("")
        self.DeleteButton_Candidate.setIcon(icon4)
        self.DeleteButton_Candidate.setIconSize(QtCore.QSize(50, 50))
        self.DeleteButton_Candidate.setObjectName("DeleteButton_Candidate")
        self.EditButton_Candidate = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton_Candidate.setGeometry(QtCore.QRect(1360, 90, 71, 51))
        self.EditButton_Candidate.setText("")
        self.EditButton_Candidate.setIcon(icon3)
        self.EditButton_Candidate.setIconSize(QtCore.QSize(50, 50))
        self.EditButton_Candidate.setObjectName("EditButton_Candidate")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1280, 140, 631, 31))
        self.frame_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_nameWindow_3 = QtWidgets.QLabel(self.frame_3)
        self.label_nameWindow_3.setGeometry(QtCore.QRect(240, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_3.setFont(font)
        self.label_nameWindow_3.setObjectName("label_nameWindow_3")
        self.SearchButton_Candidate = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton_Candidate.setGeometry(QtCore.QRect(1520, 90, 71, 51))
        self.SearchButton_Candidate.setText("")
        self.SearchButton_Candidate.setIcon(icon5)
        self.SearchButton_Candidate.setIconSize(QtCore.QSize(50, 50))
        self.SearchButton_Candidate.setObjectName("SearchButton_Candidate")
        self.tableCandidate = QtWidgets.QTableView(self.centralwidget)
        self.tableCandidate.setGeometry(QtCore.QRect(1280, 180, 631, 831))
        self.tableCandidate.setObjectName("tableCandidate")
        self.CandidateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CandidateButton.setGeometry(QtCore.QRect(1280, 90, 71, 51))
        self.CandidateButton.setText("")
        self.CandidateButton.setIcon(icon2)
        self.CandidateButton.setIconSize(QtCore.QSize(50, 50))
        self.CandidateButton.setObjectName("CandidateButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(760, 180, 511, 831))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget{font-size: 14pt;}") 
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(760, 140, 511, 31))
        self.frame_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_nameWindow_4 = QtWidgets.QLabel(self.frame_4)
        self.label_nameWindow_4.setGeometry(QtCore.QRect(150, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_4.setFont(font)
        self.label_nameWindow_4.setObjectName("label_nameWindow_4")
        self.Search_vaclineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_vaclineEdit.setGeometry(QtCore.QRect(330, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Search_vaclineEdit.setFont(font)
        self.Search_vaclineEdit.setObjectName("Search_vaclineEdit")
        self.Search_candlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_candlineEdit.setGeometry(QtCore.QRect(1600, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Search_candlineEdit.setFont(font)
        self.Search_candlineEdit.setObjectName("Search_candlineEdit")
        self.OtchotButton = QtWidgets.QPushButton(self.centralwidget)
        self.OtchotButton.setGeometry(QtCore.QRect(1100, 95, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OtchotButton.setFont(font)
        self.OtchotButton.setObjectName("OtchotButton")
        VacWindow.setCentralWidget(self.centralwidget)
        self.DeleteButton.clicked.connect(self.delete_selected_cell_and_db)
        cursor = connection.cursor()
        # Выполнение запроса к базе данных для получения данных из таблицы Vacancy и связанной таблицы Employer
        query = "SELECT Vacancy.id, Vacancy.Title, Employer.Name, Vacancy.Status FROM Vacancy INNER JOIN Employer ON Vacancy.employer = Employer.id ORDER BY CASE Vacancy.Status WHEN 'новая' THEN 1 WHEN 'неактивная' THEN 2 WHEN 'активная' THEN 3 WHEN 'закрытая' THEN 4 ELSE 5 END"
        cursor.execute(query)
        rows = cursor.fetchall()
        # Создание модели данных для таблицы
        model = QStandardItemModel(len(rows), 4)  # Определяем модель с тремя столбцами
        model.setHorizontalHeaderLabels(['ID','Наименование', 'Работодатель', 'Статус'])
        # Заполнение данными из базы данных
        for row_num, row_data in enumerate(rows):
            item_id = QStandardItem(str(row_data['id']))  # ID вакансии
            model.setItem(row_num, 0, item_id)

            item_title = QStandardItem(row_data['Title'])  # Наименование вакансии
            model.setItem(row_num, 1, item_title)

            item_employer = QStandardItem(row_data['Name'])  # Работодатель
            model.setItem(row_num, 2, item_employer)

            item_status = QStandardItem(row_data['Status'])  # Статус
            model.setItem(row_num, 3, item_status)
            if row_data['Status'] == 'Закрытая':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['Status'] == 'Неактивная':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['Status'] == 'Новая':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))


        self.tableVac.setModel(model)
# Установка модели данных для таблицы с вакансиями
        self.tableVac.setColumnWidth(0, 20)
        self.tableVac.setColumnWidth(1, 250)  # Ширина первого столбца
        self.tableVac.setColumnWidth(2, 250)  # Ширина второго столбца
        self.tableVac.setColumnWidth(3, 210)  # Ширина третьего столбца

        # Отключение возможности редактирования ячеек
        self.tableVac.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVac.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableVac.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк

        model_1 = QStandardItemModel(0, 4)  # 0 rows, 3 columns
        model_1.setHorizontalHeaderLabels(['ID','ФИ', 'Статус', 'Телефон'])

        self.tableCandidate.setModel(model_1)
        self.tableCandidate.setColumnWidth(0, 20)
        self.tableCandidate.setColumnWidth(1, 200)  # Ширина первого столбца
        self.tableCandidate.setColumnWidth(2, 200)  # Ширина второго столбца
        self.tableCandidate.setColumnWidth(3, 200)  # Ширина третьего столбца
        self.tableCandidate.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCandidate.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableCandidate.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк
        self.retranslateUi(VacWindow)
        QtCore.QMetaObject.connectSlotsByName(VacWindow)
        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(VacWindow))
        self.NewVacButton.clicked.connect(lambda: self.New_vac(VacWindow))
        self.SearchButton.clicked.connect(self.search_vac)
        self.Search_vaclineEdit.setHidden(True)
        self.tableVac.clicked.connect(lambda index: self.on_vacancy_clicked(index, VacWindow))
        self.tableVac.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Search_candlineEdit.setHidden(True)
        self.rec_kandidate_window = None 
        self.OtchotButton.clicked.connect(self.otchot)
    def on_vacancy_clicked(self, index, VacWindow):
        model = self.tableVac.model()  # Get the data model of the "Vac" table or "VacRabot" table
        vacancy_id = model.data(model.index(index.row(), 0))  # Get the vacancy ID from the selected row

        self.display_candidates_for_vacancy(vacancy_id, VacWindow)

        cursor = connection.cursor()
        sql_query = "SELECT v.title, v.salary, v.experience, v.adress, v.education, v.skills, v.date_public, emp.name \
                FROM vacancy v \
                INNER JOIN employer emp ON v.employer = emp.id \
                WHERE v.id = %s"   # Query to retrieve all data for the selected vacancy
        cursor.execute(sql_query, (vacancy_id,))  # Execute the query with the vacancy ID parameter
        result = cursor.fetchone()  # Retrieve the query result

        if result:  # If information about the vacancy is obtained
            # Clear the appropriate list widget
            self.listWidget.clear()
            self.listWidget.addItem(f"Должность: {result['title']}")
            self.listWidget.addItem(f"Работодатель: {result['name']}")
            self.listWidget.addItem(f"Зарплата: {result['salary']}")
            self.listWidget.addItem(f"Необходимый опыт работы: {result['experience']}")
            self.listWidget.addItem(f"Адрес: {result['adress']}")
            self.listWidget.addItem(f"Образование: {result['education']}")
            self.listWidget.addItem(f"Необходимые навыки: {result['skills']}")
            self.listWidget.addItem(f"Дата публикации: {result['date_public']}")

        else:
            # If information about the vacancy is not found, clear the appropriate list widget
            self.listWidget.clear()
        self.EditButton.clicked.connect(lambda: self.Edit_vac(VacWindow, vacancy_id))
        
    def search_candidate(self, vacancy_id, VacWindow):
        self.Search_candlineEdit.setHidden(False)
        search_text = self.Search_candlineEdit.text()  # Get the search text from the search line
        search_text = '%' + search_text + '%'  # Adding wildcards to search for partial matches

        cursor = connection.cursor()
        # Construct the query to search for candidates based on name and status
        sql_query = "SELECT a.id as id_app, CONCAT(a.name, ' ', a.surname) as full_name, a.status, a.telephone FROM Applicant a INNER JOIN candidate c ON a.id = c.id_app WHERE c.id_vac = %s AND (CONCAT(a.name, ' ', a.surname) LIKE %s OR a.status = %s)"
        cursor.execute(sql_query, (vacancy_id, search_text, search_text))  # Pass vacancy_id and search_text as parameters

        candidate_rows = cursor.fetchall()

        model = QStandardItemModel(len(candidate_rows), 4)  # Create a new model for the candidate table
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус', 'Телефон'])

        for row_num, row_data in enumerate(candidate_rows):
            item_id = QStandardItem(str(row_data['id_app']))  # Candidate ID
            model.setItem(row_num, 0, item_id)

            item_full_name = QStandardItem(str(row_data['full_name']))  # Candidate full name
            model.setItem(row_num, 1, item_full_name)

            item_status = QStandardItem(str(row_data['status']))  # Candidate status
            model.setItem(row_num, 2, item_status)

            item_phone = QStandardItem(str(row_data['telephone']))  # Candidate phone
            model.setItem(row_num, 3, item_phone)

        self.tableCandidate.setModel(model)  # Set the new model for the candidate table
        self.CandidateButton.clicked.connect(lambda: self.AddCand(VacWindow, vacancy_id))
        self.DeleteButton_Candidate.clicked.connect(lambda: self.DeleteCand(VacWindow, vacancy_id))
  
    def display_candidates_for_vacancy(self, vacancy_id, VacWindow):
        cursor = connection.cursor()
        # Query to retrieve candidates for the selected vacancy
        sql_query = "SELECT a.id as id_app, CONCAT(a.name, ' ', a.surname) as full_name, a.status, a.telephone FROM Applicant a INNER JOIN candidate c ON a.id = c.id_app WHERE c.id_vac = %s"
        cursor.execute(sql_query, (vacancy_id,))
        candidate_rows = cursor.fetchall()

        model = QStandardItemModel(len(candidate_rows), 4)  # Create a new model for the candidate table
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус', 'Телефон'])

        for row_num, row_data in enumerate(candidate_rows):
            item_id = QStandardItem(str(row_data['id_app']))  # Candidate ID
            model.setItem(row_num, 0, item_id)

            item_full_name = QStandardItem(row_data['full_name'])  # Candidate full name
            model.setItem(row_num, 1, item_full_name)

            item_status = QStandardItem(row_data['status'])  # Candidate status
            model.setItem(row_num, 2, item_status)

            item_phone = QStandardItem(row_data['telephone'])  # Candidate phone
            model.setItem(row_num, 3, item_phone)

        self.tableCandidate.setModel(model)  # Set the new model for the candidate table
        self.CandidateButton.clicked.connect(lambda: self.AddCand(VacWindow, vacancy_id))
        self.DeleteButton_Candidate.clicked.connect(lambda: self.DeleteCand(VacWindow, vacancy_id))
        self.SearchButton_Candidate.clicked.connect(lambda: self.search_candidate(vacancy_id, VacWindow))
        self.EditButton_Candidate.clicked.connect((lambda: self.EditSoi(VacWindow, row_data['id_app'])))


    def DeleteCand(self, VacWindow, vacancy_id):
        selected_index = self.tableCandidate.selectedIndexes()
        if selected_index:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Вы уверены, что хотите удалить эту запись?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec_() == QMessageBox.Ok:
                selected_row = selected_index[0].row()
                candidate_id = self.tableCandidate.model().index(selected_row, 0).data()
                cursor = connection.cursor()
                sql_query = "DELETE FROM Candidate WHERE id_app = %s"
                cursor.execute(sql_query, (candidate_id,))
                connection.commit()
                self.display_candidates_for_vacancy(vacancy_id, VacWindow)

    def search_vac(self):
        self.Search_vaclineEdit.setHidden(False)
        search_text = self.Search_vaclineEdit.text()  # Получаем текст для поиска
        cursor = connection.cursor()
        # Напишите запрос к базе данных с использованием search_text для поиска по фамилии и имени
        query = "SELECT Vacancy.id, Vacancy.Title, Employer.Name, Vacancy.Status FROM Vacancy INNER JOIN Employer ON Vacancy.employer = Employer.id WHERE Vacancy.title LIKE '%{0}%' OR Employer.Name LIKE '%{0}%' ORDER BY CASE WHEN Vacancy.Status = 'Новая' THEN 1 WHEN Vacancy.Status = 'Неактивная' THEN 2 WHEN Vacancy.Status = 'Активная' THEN 3 WHEN Vacancy.Status = 'Закрытая' THEN 4 ELSE 5 END".format(search_text)        
        cursor.execute(query)

        rows = cursor.fetchall()
        # Создание модели данных для таблицы
        model = QStandardItemModel(len(rows), 4)  # Определяем модель с тремя столбцами
        model.setHorizontalHeaderLabels(['ID','Наименование', 'Работодатель', 'Статус'])

        # Заполнение данными из базы данных
        for row_num, row_data in enumerate(rows):
            item_id = QStandardItem(str(row_data['id']))  # Наименование вакансии
            model.setItem(row_num, 0, item_id)

            item_title = QStandardItem(row_data['Title'])  # Наименование вакансии
            model.setItem(row_num, 1, item_title)  # Заменяем номер столбца на 0 для Наименования

            item_employer = QStandardItem(row_data['Name'])  # Работодатель
            model.setItem(row_num, 2, item_employer)  # Заменяем номер столбца на 1 для Работодателя

            item_status = QStandardItem(row_data['Status'])  # Статус
            model.setItem(row_num, 3, item_status)  # Заменяем номер столбца на 2 для Статуса
            if row_data['Status'] == 'Закрытая':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['Status'] == 'Неактивная':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['Status'] == 'Новая':
                for col in range(4):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))
        self.tableVac.setModel(model)
    def delete_selected_cell_and_db(self):
        selected_indexes = self.tableVac.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()  
            item_title = self.tableVac.model().item(row, 0)  
            title = item_title.text()  
            cursor = connection.cursor()   
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Вы уверены, что хотите удалить эту запись?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)  # Добавлена запятая здесь
            if msg.exec_() == QMessageBox.Ok:
                delete_query = "DELETE FROM Vacancy WHERE id = %s"  
                cursor.execute(delete_query, (title,))
                connection.commit()
                self.tableVac.model().removeRow(row)

    def EditSoi(self, SoiscWindow, applicant_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_anketa_soiscWindow()
        self.ui.setupUi(self.window, applicant_id)
        self.window.show()
        SoiscWindow.close()

    def otchot(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Отчёт готов!")
        msg.setInformativeText("Отчёт успешно сгенерирован. Можете найти его в папке 'Отчёты'.")
        msg.setWindowTitle("Выполнено")
        msg.exec_()
        cursor = connection.cursor()
        vacancy_query = '''
        SELECT e.name as employer, COUNT(v.id) as vacancy_count
        FROM employer e
        LEFT JOIN vacancy v ON v.employer = e.id
        GROUP BY e.name
        '''
        cursor.execute(vacancy_query)
        employers_info = cursor.fetchall()
        if not os.path.exists('Отчёты'):
            os.makedirs('Отчёты')
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        fonts.addMapping('Arial', 0, 0, 'Arial')

        doc = SimpleDocTemplate(f"Отчёты/Все_работодатели_вакансии_Отчёт_{current_date}.pdf", pagesize=(letter[1], letter[0]), encoding='utf-8')
        elements = []

        fonts.addMapping('Arial', 0, 0, 'Arial')
        # Получение стилей по умолчанию
        styles = getSampleStyleSheet()
        # Создаем стиль для заголовка с использованием подходящего шрифта
        stylesTitle = styles['Title']
        stylesTitle.fontName = 'Arial'
        stylesTitle.fontSize = 20
        # Создание текста с учетом всех улучшений
        title_text = f"Отчёт по работодателям и вакансиям на момент {current_date}"
        title = Paragraph(title_text, stylesTitle)
        elements.append(title)
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы

        with open('account.txt', 'r') as file:
            id_officer = file.read()
        sql_query = "SELECT * FROM users WHERE id_officer = %s"
        cursor.execute(sql_query, (id_officer,))
        user_data = cursor.fetchone()
        russian_style = ParagraphStyle('russian', fontName='Arial', fontSize=12, leading=12)
        agent_name = f"{user_data['surname']} {user_data['name']}"
        agent_info_text = f"Отчёт сформировал кадровый агент: {agent_name}, {user_data['telephone']}"
        agent_info = Paragraph(agent_info_text, style=russian_style)
        elements.append(agent_info)
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        # Создаем стиль для текста подписи с использованием подходящего кириллического шрифта
        signature_style = ParagraphStyle(name='SignatureStyle')
        signature_style.fontName = 'Arial'  # Используйте подходящий кириллический шрифт
        signature_style.fontSize = 12
        # Создаем текст подписи с использованием созданного стиля
        signature_text = "Подпись: ____________________"
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        signature_text = "Количество вакансий каждого работодателя, занесённых в систему, представлено в таблице 1."
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(0.5, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        # Сортировка информации о работодателях по количеству вакансий (от большего к меньшему)
        employers_info.sort(key=lambda x: x['vacancy_count'], reverse=True)

        employer_data = [['Работодатель', 'Количество вакансий']]  # Заголовки таблицы
        total_vacancies = 0
        for employer_info in employers_info:
            employer_data.append([employer_info['employer'], employer_info['vacancy_count']])
            total_vacancies += employer_info['vacancy_count']
        num_employers = len(employers_info)
        employer_data.append([f'Всего работодателей: {num_employers}', f'Всего вакансий: {total_vacancies}'])

        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        employer_table = Table(employer_data, colWidths=[3*inch, 1.5*inch])
        employer_table.setStyle(table_style)
        elements.append(employer_table)

        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        signature_text = "Количество вакансий по статусу представлено в таблице 2."
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(1, 0.3*inch))
        # Запрос информации о работодателях и количестве вакансий
        vacancy_query = '''
        SELECT e.name as employer, v.status, COUNT(v.id) as vacancy_count
        FROM employer e
        LEFT JOIN vacancy v ON v.employer = e.id
        GROUP BY e.name, v.status
        '''
        cursor.execute(vacancy_query)
        vacancies_info = cursor.fetchall()
            # Создание словаря для хранения количества вакансий в разрезе каждого статуса
        vacancy_status_count = {'Новая': 0, 'Неактивная': 0, 'Активная': 0, 'Закрытая': 0}
        for vacancy_info in vacancies_info:
            status = vacancy_info['status']
            if status in vacancy_status_count:
                vacancy_status_count[status] += vacancy_info['vacancy_count']

        # Создание таблицы с информацией о количестве вакансий по статусам
        status_data = [['Статус', 'Количество вакансий']]  # Заголовки таблицы
        for status, count in vacancy_status_count.items():
            status_data.append([status, count])

        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        status_table = Table(status_data, colWidths=[2*inch, 2*inch])
        status_table.setStyle(table_style)
        elements.append(status_table)
        elements.append(Spacer(1, 0.3*inch))
        signature_text = "Вакансии, занесённые в систему, представлены в таблице 3."
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(1, 0.3*inch))
        # Запрос информации о вакансиях с указанием статуса
        status_query = '''
        SELECT v.title as vacancy_title, v.status, v.salary, v.date_public, e.name as employer_name
        FROM vacancy v
        LEFT JOIN employer e ON v.employer = e.id
        ORDER BY
            CASE v.status
                WHEN 'Новая' THEN 1
                WHEN 'Неактивная' THEN 2
                WHEN 'Активная' THEN 3
                ELSE 4
            END'''
        cursor.execute(status_query)
        vacancies_status_info = cursor.fetchall()

        # Создание таблицы с информацией о вакансиях по статусам
        vacancy_status_data = [['Наименование вакансии', 'Статус', 'Зарплата', 'Дата публикации', 'Работодатель']]
        for vacancy_info in vacancies_status_info:
            vacancy_status_data.append([vacancy_info['vacancy_title'], vacancy_info['status'], vacancy_info['salary'], vacancy_info['date_public'], vacancy_info['employer_name']])

        status_table = Table(vacancy_status_data, colWidths=[3.3*inch, 1.5*inch, 1.5*inch, 1.5*inch, 2.7*inch])
        status_table.setStyle(table_style)
        elements.append(status_table)
        doc.build(elements)


    def BackToMainWindow(self, VacWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        VacWindow.close()

    def AddCand(self, VacWindow, vacancy_id):
        if vacancy_id is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Предупреждение")
            msg.setInformativeText("Пожалуйста, выберите вакансию перед добавлением соискателя.")
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
        else:
            if not self.rec_kandidate_window:
                self.rec_kandidate_window = QtWidgets.QMainWindow()
                self.ui = Ui_RecKandidate()
                self.ui.setupUi(self.rec_kandidate_window, vacancy_id)
            self.rec_kandidate_window.show()
            VacWindow.close()

    def New_vac(self, VacWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Vac_loading()
        self.ui.setupUi(self.window)
        self.window.show()
        VacWindow.close()

    def Edit_vac(self, VacWindow, vacancy_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditVacWindow()
        self.ui.setupUi(self.window, vacancy_id)
        self.window.show()
        VacWindow.close()

    def retranslateUi(self, VacWindow):
        _translate = QtCore.QCoreApplication.translate
        VacWindow.setWindowTitle(_translate("VacWindow", "Вакансии"))
        self.label_nameWindow.setText(_translate("VacWindow", "Вакансии"))
        self.BackButton.setText(_translate("VacWindow", "Назад"))
        self.label_nameWindow_2.setText(_translate("VacWindow", "Вакансии"))
        self.label_nameWindow_3.setText(_translate("VacWindow", "Подходящие кандидаты"))
        self.label_nameWindow_4.setText(_translate("VacWindow", "Описание выбранной вакансии"))
        self.OtchotButton.setText(_translate("VacWindow", "Отчёт"))

class Ui_SoiscWindow(object):
    def setupUi(self, SoiscWindow):
        SoiscWindow.setObjectName("VacWindow")
        SoiscWindow.setWindowModality(QtCore.Qt.NonModal)
        SoiscWindow.setEnabled(True)
        SoiscWindow.showMaximized()  # Открыть окно на весь экран

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SoiscWindow.sizePolicy().hasHeightForWidth())
        SoiscWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SoiscWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SoiscWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableSois = QtWidgets.QTableView(self.centralwidget)
        self.tableSois.setGeometry(QtCore.QRect(15, 170, 1261, 841))
        self.tableSois.setObjectName("tableSois")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1810, 0, 101, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.DescriptionSois = QtWidgets.QListWidget(self.centralwidget)
        self.DescriptionSois.setGeometry(QtCore.QRect(1280, 210, 631, 801))
        self.DescriptionSois.setStyleSheet("QListWidget{font-size: 14pt;}")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(15, 130, 1261, 31))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_nameWindow_2 = QtWidgets.QLabel(self.frame_2)
        self.label_nameWindow_2.setGeometry(QtCore.QRect(490, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_2.setFont(font)
        self.label_nameWindow_2.setObjectName("label_nameWindow_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(735, 0, 451, 51))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_nameWindow = QtWidgets.QLabel(self.frame)
        self.label_nameWindow.setGeometry(QtCore.QRect(120, 0, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_nameWindow.setFont(font)
        self.label_nameWindow.setObjectName("label_nameWindow")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(90, 70, 111, 51))
        self.EditButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditButton.setIcon(icon2)
        self.EditButton.setIconSize(QtCore.QSize(50, 50))
        self.EditButton.setObjectName("EditButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(210, 70, 71, 51))
        self.DeleteButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon3)
        self.DeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.DeleteButton.setObjectName("DeleteButton")
        self.NewSoiButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewSoiButton.setGeometry(QtCore.QRect(15, 70, 71, 51))
        self.NewSoiButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewSoiButton.setIcon(icon4)
        self.NewSoiButton.setIconSize(QtCore.QSize(50, 50))
        self.NewSoiButton.setObjectName("NewSoiButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(290, 70, 71, 51))
        self.SearchButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Pictures/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon5)
        self.SearchButton.setIconSize(QtCore.QSize(50, 50))
        self.SearchButton.setObjectName("SearchButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(1280, 130, 631, 31))
        self.frame_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_nameWindow_4 = QtWidgets.QLabel(self.frame_4)
        self.label_nameWindow_4.setGeometry(QtCore.QRect(250, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_4.setFont(font)
        self.label_nameWindow_4.setObjectName("label_nameWindow_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1280, 170, 631, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)  # Устанавливаем только для чтения
        self.lineEdit.setFont(QtGui.QFont("Arial", 10, weight=QtGui.QFont.Bold))  # Устанавливаем шрифт жирным
        self.OtchotButton = QtWidgets.QPushButton(self.centralwidget)
        self.OtchotButton.setGeometry(QtCore.QRect(1110, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OtchotButton.setFont(font)
        self.OtchotButton.setObjectName("OtchotButton")
        SoiscWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(SoiscWindow)
        QtCore.QMetaObject.connectSlotsByName(SoiscWindow)
        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(SoiscWindow))
        self.NewSoiButton.clicked.connect(lambda: self.NowSoi(SoiscWindow)) 
        self.OtchotButton.clicked.connect(self.otchotAll)
        # Подключение функции к кнопке deleteButton
        cursor = connection.cursor()  # Устанавливаем словарь для cursor, что позволит обращаться к результатам запроса по ключу
# Выполнение запроса к базе данных и склеивание столбцов Фамилия и Имя
        query = "SELECT id, CONCAT(Surname, ' ', name) AS 'ФИ', status, mail, telephone FROM Applicant ORDER BY CASE status WHEN 'Новый' THEN 1 WHEN 'Просмотрен' THEN 2 WHEN 'Подходит на вакансию' THEN 3 WHEN 'Принят на работу' THEN 4 ELSE 5 END"
        cursor.execute(query)
        result_set = cursor.fetchall()
        model = QStandardItemModel(len(result_set), 5)  # Создаем модель с четырьмя столбцами
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус','Почта' , 'Телефон'])  # Устанавливаем заголовки столбцов
        # Заполнение модели данными из результата запроса
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))  # ID
            item_id.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 0, item_id)

            item_name = QStandardItem(str(row_data['ФИ']))  # Наименование
            item_name.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 1, item_name)

            item_status = QStandardItem(str(row_data['status']))  # Дата начала сотрудничества
            item_status.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 2, item_status)

            item_mail = QStandardItem(str(row_data['mail']))  # Телефон
            item_mail.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 3, item_mail)

            item_phone = QStandardItem(str(row_data['telephone']))  # Телефон
            item_phone.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 4, item_phone)
            if row_data['status'] == 'Принят на работу':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['status'] == 'Подходит на вакансию':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['status'] == 'Новый':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))

        # Установка модели данных для таблицы
        self.tableSois.setModel(model)

        # Установка ширины столбцов
        self.tableSois.setColumnWidth(0, 20)  # Ширина третьего столбца
        self.tableSois.setColumnWidth(1, 300)  # Ширина первого столбца
        self.tableSois.setColumnWidth(2, 300)  # Ширина второго столбца
        self.tableSois.setColumnWidth(3, 300)  # Ширина третьего столбца
        self.tableSois.setColumnWidth(4, 320)  # Ширина третьего столбца

        # Отключение возможности редактирования ячеек
        self.tableSois.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSois.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableSois.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк
        self.DeleteButton.clicked.connect(self.delete_selected_cell_and_db)
                # 1. Создание виджета QLineEdit
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(370, 70, 150, 50))

            # Добавление обработчика события нажатия на кнопку "Search"
        self.SearchButton.clicked.connect(self.performSearch)

                # Добавление обработчика события выбора записи в таблице
        self.tableSois.clicked.connect(lambda index: self.showDescription(index, SoiscWindow))

        self.searchLineEdit.setHidden(True)
    # Функция для отображения описания соискателя
    def showDescription(self, index, SoiscWindow):
        cursor = connection.cursor()
        selected_row = index.row()  # Получаем номер выбранной строки
        applicant_id = self.tableSois.model().index(selected_row, 0).data()  # Получаем id выбранного соискателя

        cursor = connection.cursor()
        sql_query = "SELECT * FROM applicant WHERE id = %s"  # Запрос на получение всех данных выбранной вакансии
        cursor.execute(sql_query, (applicant_id,))  # Выполняем запрос с параметром vacancy_id
        result = cursor.fetchone()  # Получаем результат запроса

        if result:  # Проверяем, получена ли информация о вакансии
            # Очищаем QListWidget
            self.DescriptionSois.clear()
            
            self.DescriptionSois.addItem(f"Имя: {result['name']}")
            self.DescriptionSois.addItem(f"Фамилия: {result['surname']}")
            self.DescriptionSois.addItem(f"Дата рождения: {result['date_of_birth']}")
            self.DescriptionSois.addItem(f"Телефон: {result['telephone']}")
            self.DescriptionSois.addItem(f"Почта: {result['mail']}")
            self.DescriptionSois.addItem(f"Город проживания: {result['city']}")
            self.DescriptionSois.addItem(f"Годы работы: {result['year_ex']}")
            self.DescriptionSois.addItem(f"Место работы: {result['place_ex']}")
            self.DescriptionSois.addItem(f"Годы образования: {result['year_educ']}")
            self.DescriptionSois.addItem(f"Место образования: {result['place_educ']}")
            self.DescriptionSois.addItem(f"Специализация: {result['special']}")
            self.DescriptionSois.addItem(f"Навыки: {result['skills']}")


            self.lineEdit.setText(f"Статус: {result['status']}")
            self.EditButton.clicked.connect(lambda: self.EditSoi(SoiscWindow, applicant_id))

        else:
            # Если информация о вакансии не найдена, очищаем QListWidget
            self.DescriptionSois.clear()
    # Функция для выполнения поиска и отображения результатов
    def performSearch(self):
        self.searchLineEdit.setHidden(False)
        search_text = self.searchLineEdit.text()  # Получаем текст для поиска
        cursor = connection.cursor()
        # Напишите запрос к базе данных с использованием search_text для поиска по фамилии и имени
        query = "SELECT id, CONCAT(Surname, ' ', name) AS 'ФИ', status, mail, telephone FROM Applicant WHERE Surname LIKE '%{0}%' OR name LIKE '%{0}%' ORDER BY CASE status WHEN 'Новый' THEN 1 WHEN 'Просмотрен' THEN 2 WHEN 'Подходит на вакансию' THEN 3 WHEN 'Принят на работу' THEN 4 ELSE 5 END".format(search_text)

        cursor.execute(query)
        result_set = cursor.fetchall()

        # Обновляем модель данных таблицы с результатами поиска
        model = QStandardItemModel(len(result_set), 5)  # Создаем модель с четырьмя столбцами
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус','Почта' , 'Телефон'])  # Устанавливаем заголовки столбцов

        # Заполнение модели данными из результата запроса
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))  # ID
            item_id.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 0, item_id)

            item_name = QStandardItem(str(row_data['ФИ']))  # Наименование
            item_name.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 1, item_name)

            item_status = QStandardItem(str(row_data['status']))  # Дата начала сотрудничества
            item_status.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 2, item_status)

            item_mail = QStandardItem(str(row_data['mail']))  # Телефон
            item_mail.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 3, item_mail)

            item_phone = QStandardItem(str(row_data['telephone']))  # Телефон
            item_phone.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 4, item_phone)
            if row_data['status'] == 'Принят на работу':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['status'] == 'Подходит на вакансию':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['status'] == 'Новый':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))

        self.tableSois.setModel(model)  # Устанавливаем новую модель данных для таблицы

    def delete_selected_cell_and_db(self):
        selected_indexes = self.tableSois.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()  # Получаем индекс строки выбранной ячейки
            item = self.tableSois.model().item(row, 0)  # Получаем выбранный элемент ФИО
            fio = item.text()  # Получаем значение ФИО

            # Добавление диалогового окна для подтверждения удаления
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Вы уверены, что хотите удалить эту запись?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec_() == QMessageBox.Ok:
                # Удаление данных из базы данных соответствующей выбранной записи
                cursor = connection.cursor()
                delete_query = "DELETE FROM Applicant WHERE id = %s"  # Удаляем запись, соответствующую выбранному ФИО
                cursor.execute(delete_query, (fio,))
                connection.commit()
                # Удаление выбранной строки из таблицы
                self.tableSois.model().removeRow(row)

    def BackToMainWindow(self, SoiscWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        SoiscWindow.close()

    def NowSoi(self, SoiscWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_load_ankets()
        self.ui.setupUi(self.window)
        self.window.show()
        SoiscWindow.close()

    def EditSoi(self, SoiscWindow, applicant_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_anketa_soiscWindow()
        self.ui.setupUi(self.window, applicant_id)
        self.window.show()
        SoiscWindow.close()
 
    def otchotAll(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Отчёт готов!")
        msg.setInformativeText("Отчёт успешно сгенерирован. Можете найти его в папке 'Отчёты'.")
        msg.setWindowTitle("Выполнено")
        msg.exec_()
        cursor = connection.cursor()
        cursor.execute("SELECT status, name, surname, date_of_birth, telephone, mail, city FROM Applicant ORDER BY status")
        applicants_by_status = cursor.fetchall()
        # Создание директории "Отчёты", если она не существует
        if not os.path.exists('Отчёты'):
            os.makedirs('Отчёты')
        # Получение текущей даты
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # Установка шрифта для поддержки русского текста
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        fonts.addMapping('Arial', 0, 0, 'Arial')  # Для русских символов
        # Создание PDF-файла в директории "Отчёты" с текущей датой в названии
        doc = SimpleDocTemplate(f"Отчёты/Все_соискатели_Отчёт_{current_date}.pdf", pagesize=(letter[1], letter[0]), encoding='utf-8')
        elements = []
                # Устанавливаем подходящий шрифт, поддерживающий кириллические символы
        fonts.addMapping('Arial', 0, 0, 'Arial')
        # Получение стилей по умолчанию
        styles = getSampleStyleSheet()
        # Создаем стиль для заголовка с использованием подходящего шрифта
        stylesTitle = styles['Title']
        stylesTitle.fontName = 'Arial'
        stylesTitle.fontSize = 20
        # Создание текста с учетом всех улучшений
        title_text = f"Отчёт по соискателям на момент {current_date}"
        title = Paragraph(title_text, stylesTitle)
        elements.append(title)
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        # Добавление информации о соискателях в таблицу
        data = [['Статус', 'Имя', 'Фамилия', 'Дата рождения', 'Телефон', 'Email', 'Город']]  # Заголовки таблицы
        for applicant in applicants_by_status:
            data.append([applicant['status'], applicant['name'], applicant['surname'], applicant['date_of_birth'], applicant['telephone'], applicant['mail'], applicant['city']])
        total_applicants = len(applicants_by_status)
        data.append(['', '', '', '', '', '', f'Всего соискателей: {total_applicants}'])
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        with open('account.txt', 'r') as file:
            id_officer = file.read()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_query = "SELECT * FROM users WHERE id_officer = %s"
            cursor.execute(sql_query, (id_officer,))
            user_data = cursor.fetchone()
            russian_style = ParagraphStyle('russian', fontName='Arial', fontSize=12, leading=12)
            agent_name = f"{user_data['surname']} {user_data['name']}"
            agent_info_text = f"Отчёт сформировал кадровый агент: {agent_name}, {user_data['telephone']}"
            agent_info = Paragraph(agent_info_text, style=russian_style)
            elements.append(agent_info)
        elements.append(Spacer(1, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        # Создаем стиль для текста подписи с использованием подходящего кириллического шрифта
        signature_style = ParagraphStyle(name='SignatureStyle')
        signature_style.fontName = 'Arial'  # Используйте подходящий кириллический шрифт
        signature_style.fontSize = 12
        # Создаем текст подписи с использованием созданного стиля
        signature_text = "Подпись: ____________________"
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(0.5, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        signature_text = "Количество соискателей по статусам представлено в таблице 1."
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(0.5, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        table = Table(data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch, 1.8*inch, 1.5*inch])
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)
        status_counts = {}
        for applicant in applicants_by_status:
            status = applicant['status']
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

        status_count_data = [['Статус', 'Количество']]
        for status, count in status_counts.items():
            status_count_data.append([status, count])
        status_count_table = Table(status_count_data, colWidths=[1.5*inch, 1.5*inch])
        status_count_table.setStyle(style)
        elements.append(status_count_table)
        elements.append(Spacer(0.5, 0.5*inch))  # Создание промежутка в 0.5 дюйма после первой таблицы
        signature_text = "Соискатели, занесённые в систему, представлены в таблице 2."
        signature = Paragraph(signature_text, signature_style)
        elements.append(signature)
        elements.append(Spacer(1, 0.5*inch))

        for i in range(len(data)):
            for j in range(len(data[i])):
                table.setStyle(TableStyle([('FONTNAME', (j, i), (j, i), 'Arial')]))
        elements.append(table)
        doc.build(elements)

    def retranslateUi(self, SoiscWindow):
        _translate = QtCore.QCoreApplication.translate
        SoiscWindow.setWindowTitle(_translate("SoiscWindow", "Соискатели"))
        self.BackButton.setText(_translate("SoiscWindow", "Назад"))
        self.label_nameWindow_2.setText(_translate("SoiscWindow", "Соискатели"))
        self.label_nameWindow.setText(_translate("SoiscWindow", "Соискатели"))
        self.label_nameWindow_4.setText(_translate("SoiscWindow", "Описание соискателя"))
        self.OtchotButton.setText(_translate("SoiscWindow", "Отчёт"))


class Ui_RabotWindow(object):
    def setupUi(self, RabotWindow):
        RabotWindow.setObjectName("RabotWindow")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RabotWindow.sizePolicy().hasHeightForWidth())
        RabotWindow.setSizePolicy(sizePolicy)
        RabotWindow.showMaximized() 

        self.centralwidget = QtWidgets.QWidget(RabotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableRabotodatel = QtWidgets.QTableView(self.centralwidget)
        self.tableRabotodatel.setGeometry(QtCore.QRect(10, 170, 631, 820))
        self.tableRabotodatel.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableRabotodatel.setGridStyle(QtCore.Qt.NoPen)
        self.tableRabotodatel.setObjectName("tableRabotodatel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1810, 10, 101, 61))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RabotWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RabotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableRabotodatel = QtWidgets.QTableView(self.centralwidget)
        self.tableRabotodatel.setGeometry(QtCore.QRect(10, 170, 631, 820))
        self.tableRabotodatel.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableRabotodatel.setGridStyle(QtCore.Qt.NoPen)
        self.tableRabotodatel.setObjectName("tableRabotodatel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1810, 10, 101, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.Description_vac = QtWidgets.QListWidget(self.centralwidget)
        self.Description_vac.setGeometry(QtCore.QRect(1390, 170, 511, 820))
        self.Description_vac.setObjectName("Description_vac")
        self.Description_vac.setStyleSheet("QListWidget{font-size: 14pt;}")
        self.SearchButton_Vac = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton_Vac.setGeometry(QtCore.QRect(820, 80, 71, 51))
        self.SearchButton_Vac.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton_Vac.setIcon(icon2)
        self.SearchButton_Vac.setIconSize(QtCore.QSize(50, 50))
        self.SearchButton_Vac.setObjectName("SearchButton_Vac")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 130, 631, 31))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_nameWindow_2 = QtWidgets.QLabel(self.frame_2)
        self.label_nameWindow_2.setGeometry(QtCore.QRect(260, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_2.setFont(font)
        self.label_nameWindow_2.setObjectName("label_nameWindow_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(790, 0, 451, 51))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_nameWindow = QtWidgets.QLabel(self.frame)
        self.label_nameWindow.setGeometry(QtCore.QRect(90, 0, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_nameWindow.setFont(font)
        self.label_nameWindow.setObjectName("label_nameWindow")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(80, 80, 101, 51))
        self.EditButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditButton.setIcon(icon3)
        self.EditButton.setIconSize(QtCore.QSize(50, 50))
        self.EditButton.setObjectName("EditButton")
        self.tableVacRabot = QtWidgets.QTableView(self.centralwidget)
        self.tableVacRabot.setGeometry(QtCore.QRect(650, 170, 731, 941))
        self.tableVacRabot.setObjectName("tableVacRabot")
        self.EditButton_Vac = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton_Vac.setGeometry(QtCore.QRect(650, 80, 101, 51))
        self.EditButton_Vac.setText("")
        self.EditButton_Vac.setIcon(icon3)
        self.EditButton_Vac.setIconSize(QtCore.QSize(50, 50))
        self.EditButton_Vac.setObjectName("EditButton_Vac")
        self.DeleteButton_Vac = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton_Vac.setGeometry(QtCore.QRect(750, 80, 71, 51))
        self.DeleteButton_Vac.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton_Vac.setIcon(icon4)
        self.DeleteButton_Vac.setIconSize(QtCore.QSize(50, 50))
        self.DeleteButton_Vac.setObjectName("DeleteButton_Vac")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(180, 80, 71, 51))
        self.DeleteButton.setText("")
        self.DeleteButton.setIcon(icon4)
        self.DeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.DeleteButton.setObjectName("DeleteButton")
        self.NewRabButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewRabButton.setGeometry(QtCore.QRect(10, 80, 71, 51))
        self.NewRabButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewRabButton.setIcon(icon5)
        self.NewRabButton.setIconSize(QtCore.QSize(50, 50))
        self.NewRabButton.setObjectName("NewRabButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(250, 80, 71, 51))
        self.SearchButton.setText("")
        self.SearchButton.setIcon(icon2)
        self.SearchButton.setIconSize(QtCore.QSize(50, 50))
        self.SearchButton.setObjectName("SearchButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(1390, 130, 511, 31))
        self.frame_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_nameWindow_4 = QtWidgets.QLabel(self.frame_4)
        self.label_nameWindow_4.setGeometry(QtCore.QRect(140, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_4.setFont(font)
        self.label_nameWindow_4.setObjectName("label_nameWindow_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(650, 130, 731, 31))
        self.frame_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_nameWindow_3 = QtWidgets.QLabel(self.frame_3)
        self.label_nameWindow_3.setGeometry(QtCore.QRect(290, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_3.setFont(font)
        self.label_nameWindow_3.setObjectName("label_nameWindow_3")
        RabotWindow.setCentralWidget(self.centralwidget)
        self.Search_rabEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_rabEdit.setGeometry(QtCore.QRect(330, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Search_rabEdit.setFont(font)
        self.Search_rabEdit.setObjectName("Search_rabEdit")
        self.Search_VacEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_VacEdit.setGeometry(QtCore.QRect(900, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Search_VacEdit.setFont(font)
        self.Search_VacEdit.setObjectName("Search_VacEdit")

        self.Search_rabEdit.setHidden(True)
        self.Search_VacEdit.setHidden(True)

        self.retranslateUi(RabotWindow)
        QtCore.QMetaObject.connectSlotsByName(RabotWindow)

        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(RabotWindow))
        self.NewRabButton.clicked.connect(lambda: self.New_rab(RabotWindow))
        
        
        self.DeleteButton.clicked.connect(self.delete_selected_cell_and_db)
        self.DeleteButton_Vac.clicked.connect(self.delete_vac)


        cursor = connection.cursor()
        sql_query = "SELECT id, Telephone, Name, date_start FROM employer"  # Добавляем столбец "id" в запрос
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        model = QStandardItemModel(len(result_set), 4)  # Создаем модель с четырьмя столбцами
        model.setHorizontalHeaderLabels(['ID', 'Наименование', 'Дата начала сотрудничества', 'Телефон'])  # Устанавливаем заголовки столбцов

        # Заполнение модели данными из результата запроса
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))  # ID
            item_id.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 0, item_id)

            item_name = QStandardItem(row_data['Name'])  # Наименование
            item_name.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 1, item_name)

            item_date_start = QStandardItem(str(row_data['date_start']))  # Дата начала сотрудничества
            item_date_start.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 2, item_date_start)

            item_phone = QStandardItem(str(row_data['Telephone']))  # Телефон
            item_phone.setTextAlignment(Qt.AlignHCenter)  # Выравнивание по центру
            model.setItem(row_num, 3, item_phone)

        self.tableRabotodatel.setModel(model)
        # Установка ширины столбцов
        self.tableRabotodatel.setColumnWidth(0, 20) 
        self.tableRabotodatel.setColumnWidth(1, 200)  
        self.tableRabotodatel.setColumnWidth(2, 200)
        self.tableRabotodatel.setColumnWidth(3, 200) 

        # Отключение возможности редактирования ячеек
        self.tableRabotodatel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableRabotodatel.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableRabotodatel.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк

        self.tableRabotodatel.clicked.connect(lambda index: self.on_employer_clicked(index, RabotWindow))



        self.model_1 = QStandardItemModel(0, 4)  # 0 rows, 3 columns
        self.model_1.setHorizontalHeaderLabels(['ID','Наименование', 'Дата публикации', 'Статус'])

        self.tableVacRabot.setModel(self.model_1)
        self.tableVacRabot.setColumnWidth(0, 20)  # Ширина третьего столбца
        self.tableVacRabot.setColumnWidth(1, 310)  # Ширина первого столбца
        self.tableVacRabot.setColumnWidth(2, 200)  # Ширина второго столбца
        self.tableVacRabot.setColumnWidth(3, 200)  # Ширина третьего столбца
        self.tableVacRabot.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVacRabot.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableVacRabot.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк

        self.tableVacRabot.clicked.connect(lambda index: self.on_vacancy_clicked(index, RabotWindow))
        
        self.SearchButton.clicked.connect(self.rabSearch)
        self.SearchButton_Vac.clicked.connect(self.vacSearch)
        

    def on_employer_clicked(self, index, RabotWindow):
        model = self.tableRabotodatel.model()  # Получаем модель данных таблицы "Работодатели"
        employer_id = model.data(model.index(index.row(), 0))  # Получаем идентификатор работодателя из выбранной строки

        cursor = connection.cursor()
        sql_query = "SELECT id, Title, date_public, status FROM vacancy WHERE employer = %s"  # Запрос на выборку вакансий для выбранного работодателя
        cursor.execute(sql_query, (employer_id,))  # Выполняем запрос с параметром employer_id
        result_set = cursor.fetchall()

        model_vacancy = QStandardItemModel(len(result_set), 4)  # Создаем модель с количеством строк, равным количеству полученных записей, и четырьмя столбцами
        model_vacancy.setHorizontalHeaderLabels(['ID', 'Наименование', 'Дата публикации', 'Статус'])  # Устанавливаем заголовки столбцов
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))  # ID вакансии
            model_vacancy.setItem(row_num, 0, item_id)

            item_name = QStandardItem(row_data['Title'])  # Наименование
            model_vacancy.setItem(row_num, 1, item_name)

            item_date_public = QStandardItem(str(row_data['date_public']))  # Дата публикации
            model_vacancy.setItem(row_num, 2, item_date_public)

            item_status = QStandardItem(row_data['status'])  # Статус
            model_vacancy.setItem(row_num, 3, item_status)

        self.tableVacRabot.setModel(model_vacancy)  # Устанавливаем новую модель в таблицу "Вакансии"
        self.EditButton.clicked.connect(lambda: self.Edit_rab(RabotWindow, employer_id))

    def on_vacancy_clicked(self, index, RabotWindow):
        model = self.tableVacRabot.model()  # Получаем модель данных таблицы "Вакансии работодателя"
        vacancy_id = model.data(model.index(index.row(), 0))  # Получаем идентификатор вакансии из выбранной строки

        cursor = connection.cursor()
        sql_query = "SELECT * FROM vacancy WHERE id = %s"  # Запрос на получение всех данных выбранной вакансии
        cursor.execute(sql_query, (vacancy_id,))  # Выполняем запрос с параметром vacancy_id
        result = cursor.fetchone()  # Получаем результат запроса

        if result:  # Проверяем, получена ли информация о вакансии
            # Очищаем QListWidget
            self.Description_vac.clear()
            
            self.Description_vac.addItem(f"Название: {result['title']}")
            self.Description_vac.addItem(f"Зарплата: {result['salary']}")
            self.Description_vac.addItem(f"Необходимый опыт работы: {result['experience']}")
            self.Description_vac.addItem(f"Адрес: {result['adress']}")
            self.Description_vac.addItem(f"Образование: {result['education']}")
            self.Description_vac.addItem(f"Необходимые навыки: {result['skills']}")
            self.Description_vac.addItem(f"Дата публикации: {result['date_public']}")

        else:
            # Если информация о вакансии не найдена, очищаем QListWidget
            self.Description_vac.clear()
        self.EditButton_Vac.clicked.connect(lambda: self.Edit_vac(RabotWindow, vacancy_id))

    def rabSearch(self):
        self.Search_rabEdit.setHidden(False)
        search_text = self.Search_rabEdit.text()  # Получаем текст для поиска
        cursor = connection.cursor()
        # Напишите запрос к базе данных с использованием search_text для поиска по фамилии и имени
        query = "SELECT id, name, date_start, telephone FROM Employer WHERE Name LIKE '%{0}%'".format(search_text)
        cursor.execute(query)
        result_set = cursor.fetchall()

        model_vacancy = QStandardItemModel(len(result_set), 4)  # Создаем модель с количеством строк, равным количеству полученных записей, и четырьмя столбцами
        model_vacancy.setHorizontalHeaderLabels(['ID', 'Наименование', 'Дата начала сотрудничества', 'Телефон'])  # Устанавливаем заголовки столбцов
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))  # ID вакансии
            model_vacancy.setItem(row_num, 0, item_id)

            item_name = QStandardItem(row_data['name'])  # Наименование
            model_vacancy.setItem(row_num, 1, item_name)

            item_date_public = QStandardItem(str(row_data['date_start']))  # Дата публикации
            model_vacancy.setItem(row_num, 2, item_date_public)

            item_status = QStandardItem(row_data['telephone'])  # Статус
            model_vacancy.setItem(row_num, 3, item_status)

        self.tableRabotodatel.setModel(model_vacancy)

    def vacSearch(self):
        self.Search_VacEdit.setHidden(False)
        search_text = self.Search_VacEdit.text()
        
        if not self.tableRabotodatel.selectedIndexes():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Пожалуйста, выберите работодателя, у которого вы хотели осуществить поиск вакансии")
            msg.setWindowTitle("Не выбран работодатель")
            msg.exec_()
            return
        
        model = self.tableRabotodatel.model()

        selected_row = self.tableRabotodatel.selectedIndexes()[0].row()
        employer_id = model.data(model.index(selected_row, 0)) 

        cursor = connection.cursor()
        query = "SELECT id, title, date_public, status FROM Vacancy WHERE title LIKE %s AND employer = %s"
        cursor.execute(query, ('%' + search_text + '%', employer_id))
        result_set = cursor.fetchall()

        model_vacancy = QStandardItemModel(len(result_set), 4)
        model_vacancy.setHorizontalHeaderLabels(['ID', 'Наименование', 'Дата публикации', 'Статус'])

        # Populate the model with the data from the query result
        for row_num, row_data in enumerate(result_set):
            item_id = QStandardItem(str(row_data['id']))
            model_vacancy.setItem(row_num, 0, item_id)

            item_title = QStandardItem(row_data['title'])
            model_vacancy.setItem(row_num, 1, item_title)

            item_date_public = QStandardItem(str(row_data['date_public']))
            model_vacancy.setItem(row_num, 2, item_date_public)

            item_status = QStandardItem(row_data['status'])
            model_vacancy.setItem(row_num, 3, item_status)
            if row_data['status'] == 'Принят на работу':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['status'] == 'Подходит на вакансию':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['status'] == 'Новый':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))

        self.tableVacRabot.setModel(model_vacancy)  # Set the new model in the "Вакансии" table

    def delete_selected_cell_and_db(self):
        selected_indexes = self.tableRabotodatel.selectedIndexes()
        if selected_indexes:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Вы уверены, что хотите удалить эту запись?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setWindowTitle("Подтверждение удаления")

            if msg.exec_() == QMessageBox.Yes:
                row = selected_indexes[0].row()  # Получаем индекс строки выбранной ячейки
                item = self.tableRabotodatel.model().item(row, 0)  # Получаем выбранный элемент Наименование
                title = item.text()  # Получаем значение name

                # Удаление данных из базы данных соответствующей выбранной записи
                cursor = connection.cursor()
                delete_query = "DELETE FROM Employer WHERE id = %s"  # Удаляем запись, соответствующую выбранному name
                cursor.execute(delete_query, (title,))
                connection.commit()

                # Удаление выбранной строки из таблицы
                self.tableRabotodatel.model().removeRow(row)
    def delete_vac(self):
        selected_indexes = self.tableVacRabot.selectedIndexes()
        if selected_indexes:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Вы уверены, что хотите удалить эту запись?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setWindowTitle("Подтверждение удаления")

            if msg.exec_() == QMessageBox.Yes:
                row = selected_indexes[0].row()  # Получаем индекс строки выбранной ячейки
                item = self.tableVacRabot.model().item(row, 0)  # Получаем выбранный элемент Наименование
                title = item.text()  # Получаем значение name

                # Удаление данных из базы данных соответствующей выбранной записи
                cursor = connection.cursor()
                delete_query = "DELETE FROM Vacancy WHERE id = %s"  # Удаляем запись, соответствующую выбранному name
                cursor.execute(delete_query, (title,))
                connection.commit()

                # Удаление выбранной строки из таблицы
                self.tableVacRabot.model().removeRow(row)
        
    def BackToMainWindow(self, VacWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        VacWindow.close()

    def New_rab(self, VacWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rab_loading()
        self.ui.setupUi(self.window)
        self.window.show()
        VacWindow.close()

    def Edit_vac(self, VacWindow, vacancy_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditVacWindow()
        self.ui.setupUi(self.window, vacancy_id)
        self.window.show()
        VacWindow.close()

    def Edit_rab(self, VacWindow, employer_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rab_edit()
        self.ui.setupUi(self.window, employer_id)
        self.window.show()
        VacWindow.close()

    def retranslateUi(self, RabotWindow):
        _translate = QtCore.QCoreApplication.translate
        RabotWindow.setWindowTitle(_translate("RabotWindow", "Работодатель"))
        self.BackButton.setText(_translate("RabotWindow", "Назад"))
        self.label_nameWindow_2.setText(_translate("RabotWindow", "Работодатели"))
        self.label_nameWindow.setText(_translate("RabotWindow", "Работодатели"))
        self.label_nameWindow_4.setText(_translate("RabotWindow", "Описание выбранной вакансии"))
        self.label_nameWindow_3.setText(_translate("RabotWindow", "Вакансии работодателя"))



class Ui_Vac_loading(object):
    def setupUi(self, Vac_loading):
        Vac_loading.setObjectName("Vac_loading")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vac_loading.sizePolicy().hasHeightForWidth())
        Vac_loading.setSizePolicy(sizePolicy)
        Vac_loading.showMaximized() 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Vac_loading.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Vac_loading)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(610, 0, 721, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1760, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(859, 100, 601, 601))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(120, 0, 391, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(119, 70, 391, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VacTitleEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.VacTitleEdit.setText("")
        self.VacTitleEdit.setObjectName("VacTitleEdit")
        self.verticalLayout_2.addWidget(self.VacTitleEdit)
        self.SalaryEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SalaryEdit.setText("")
        self.SalaryEdit.setObjectName("SalaryEdit")
        self.verticalLayout_2.addWidget(self.SalaryEdit)
        self.ExperienceEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ExperienceEdit.setText("")
        self.ExperienceEdit.setObjectName("ExperienceEdit")
        self.verticalLayout_2.addWidget(self.ExperienceEdit)
        self.AdressEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.AdressEdit.setText("")
        self.AdressEdit.setObjectName("AdressEdit")
        self.verticalLayout_2.addWidget(self.AdressEdit)
        self.Level_educationEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Level_educationEdit.setText("")
        self.Level_educationEdit.setObjectName("Level_educationEdit")
        self.verticalLayout_2.addWidget(self.Level_educationEdit)
        self.skillsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.skillsEdit.setText("")
        self.skillsEdit.setObjectName("skillsEdit")
        self.verticalLayout_2.addWidget(self.skillsEdit)
        self.publishButton = QtWidgets.QPushButton(self.centralwidget)
        self.publishButton.setGeometry(QtCore.QRect(1190, 750, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.publishButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.publishButton.setIcon(icon2)
        self.publishButton.setObjectName("publishButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 100, 501, 771))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 10, 391, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.AddSois = QtWidgets.QPushButton(self.frame_2)
        self.AddSois.setGeometry(QtCore.QRect(160, 160, 171, 28))
        self.AddSois.setObjectName("AddSois")

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(50, 111, 391, 31))
        self.comboBox.setObjectName("comboBox")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(240, 140, 121, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 190, 391, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RabotNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.RabotNameEdit.setText("")
        self.RabotNameEdit.setObjectName("RabotNameEdit")
        self.verticalLayout.addWidget(self.RabotNameEdit)
        self.AdressRabEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AdressRabEdit.setFont(font)
        self.AdressRabEdit.setText("")
        self.AdressRabEdit.setObjectName("AdressRabEdit")
        self.verticalLayout.addWidget(self.AdressRabEdit)
        self.PhoneNumberEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PhoneNumberEdit.setText("")
        self.PhoneNumberEdit.setObjectName("PhoneNumberEdit")
        self.verticalLayout.addWidget(self.PhoneNumberEdit)
        self.MailEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.MailEdit.setText("")
        self.MailEdit.setObjectName("MailEdit")
        self.verticalLayout.addWidget(self.MailEdit)
        self.ClearButton = QtWidgets.QPushButton(self.frame_2)
        self.ClearButton.setGeometry(QtCore.QRect(60, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon3)
        self.ClearButton.setObjectName("ClearButton")
        self.SaveButton = QtWidgets.QPushButton(self.frame_2)
        self.SaveButton.setGeometry(QtCore.QRect(260, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveButton.setFont(font)
        self.SaveButton.setIcon(icon2)
        self.SaveButton.setObjectName("SaveButton")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(50, 420, 391, 191))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(60, 10, 261, 31))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(50, 0, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Surname_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Surname_edit.setGeometry(QtCore.QRect(60, 60, 261, 31))
        self.Surname_edit.setObjectName("Surname_edit")
        self.Name_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Name_edit.setGeometry(QtCore.QRect(60, 110, 261, 31))
        self.Name_edit.setObjectName("Name_edit")
        self.ClearVac_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ClearVac_Button.setGeometry(QtCore.QRect(860, 750, 291, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearVac_Button.setFont(font)
        self.ClearVac_Button.setIcon(icon3)
        self.ClearVac_Button.setObjectName("ClearVac_Button")
        Vac_loading.setCentralWidget(self.centralwidget)
        self.ChooseSoisBtn = QtWidgets.QPushButton(self.frame_2)
        self.ChooseSoisBtn.setGeometry(QtCore.QRect(160, 110, 171, 28))
        self.ChooseSoisBtn.setObjectName("ChooseSoisBtn")

        self.retranslateUi(Vac_loading)
        QtCore.QMetaObject.connectSlotsByName(Vac_loading)

        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(Vac_loading))
        self.ClearButton.clicked.connect(self.clearFields)
        self.ClearVac_Button.clicked.connect(self.clear_applicant)
        self.SaveButton.clicked.connect(self.saveEmployerData)
        self.publishButton.clicked.connect(self.saveVacancyData)
        self.ChooseSoisBtn.clicked.connect(self.showCombo)
        

        self.RabotNameEdit.setToolTip("Наименование работодателя")
        self.AdressRabEdit.setToolTip("Адрес работодателя")
        self.PhoneNumberEdit.setToolTip("Номер телефона")
        self.MailEdit.setToolTip("Адрес электронной почты")
        self.Surname_edit.setToolTip("Фамилия ответственного лица")
        self.Name_edit.setToolTip("Имя ответственного лица")
        self.VacTitleEdit.setToolTip("Наименование вакансии")
        self.SalaryEdit.setToolTip("Зарплата")
        self.ExperienceEdit.setToolTip("Опыт работы")
        self.AdressEdit.setToolTip("Адрес работы")
        self.Level_educationEdit.setToolTip("Уровень образования")
        self.skillsEdit.setToolTip("Необходимые навыки")

        self.AddSois.clicked.connect(self.showFields)
        self.RabotNameEdit.setHidden(True)
        self.AdressRabEdit.setHidden(True)
        self.PhoneNumberEdit.setHidden(True)
        self.MailEdit.setHidden(True)
        self.Surname_edit.setHidden(True)
        self.Name_edit.setHidden(True)
        self.SaveButton.setHidden(True)
        self.ClearButton.setHidden(True)
        self.frame_6.setHidden(True)
        self.frame_7.setHidden(True)
        self.label_6.setHidden(True)
        self.ChooseSoisBtn.setHidden(True)

        self.fill_employer_combobox()

    def fill_employer_combobox(self):
        cursor = connection.cursor()
        sql_query = "SELECT id, name FROM Employer"  # Query to retrieve employer id and names
        cursor.execute(sql_query)  # Execute the query
        result_set = cursor.fetchall()  # Retrieve the query result
        connection.commit()

        # Clear the combobox to avoid duplicate entries
        self.comboBox.clear()

        # Add employer id and names to the combobox
        for row in result_set:
            employer_id = row['id']
            employer_name = row['name']
            self.comboBox.addItem(f"{employer_id} - {employer_name}")  # Adding both id and name together as an item




    def showFields(self):
        self.RabotNameEdit.setHidden(False)
        self.AdressRabEdit.setHidden(False)
        self.PhoneNumberEdit.setHidden(False)
        self.MailEdit.setHidden(False)
        self.Surname_edit.setHidden(False)
        self.Name_edit.setHidden(False)
        self.SaveButton.setHidden(False)
        self.ClearButton.setHidden(False)
        self.AddSois.setHidden(True)
        self.frame_6.setHidden(False)
        self.frame_7.setHidden(False)
        self.label_6.setHidden(False)
        self.comboBox.setHidden(True)
        self.label_3.setHidden(True)
        self.ChooseSoisBtn.setHidden(False)

    def showCombo(self):
        self.RabotNameEdit.setHidden(True)
        self.AdressRabEdit.setHidden(True)
        self.PhoneNumberEdit.setHidden(True)
        self.MailEdit.setHidden(True)
        self.Surname_edit.setHidden(True)
        self.Name_edit.setHidden(True)
        self.SaveButton.setHidden(True)
        self.ClearButton.setHidden(True)
        self.AddSois.setHidden(False)
        self.frame_6.setHidden(True)
        self.frame_7.setHidden(True)
        self.label_6.setHidden(True)
        self.comboBox.setHidden(False)
        self.label_3.setHidden(False)
        self.ChooseSoisBtn.setHidden(True)


    def toggleInputFields(self, state):
        if state == Qt.Checked:
            self.RabotNameEdit.setEnabled(True)
            self.AdressRabEdit.setEnabled(True)
            self.PhoneNumberEdit.setEnabled(True)
            self.MailEdit.setEnabled(True)
            self.Surname_edit.setEnabled(True)
            self.Name_edit.setEnabled(True)
        else:
            self.RabotNameEdit.setEnabled(False)
            self.AdressRabEdit.setEnabled(False)
            self.PhoneNumberEdit.setEnabled(False)
            self.MailEdit.setEnabled(False)
            self.Surname_edit.setEnabled(False)
            self.Name_edit.setEnabled(False)


    def saveEmployerData(self):
        if (self.RabotNameEdit.text() and self.AdressRabEdit.text() and self.PhoneNumberEdit.text() 
        and self.MailEdit.text() and self.Surname_edit.text() and self.Name_edit.text()):

            # Получение введенных пользователем данных
            rabot_name = self.RabotNameEdit.text()
            address = self.AdressRabEdit.text()
            phone_number = self.PhoneNumberEdit.text()
            email = self.MailEdit.text()
            responsible_surname = self.Surname_edit.text()
            responsible_name = self.Name_edit.text()

            # Получение текущей даты
            date_start = datetime.datetime.now().date()

            # Подключение к базе данных
            cursor = connection.cursor()

            # Создание SQL-запроса для добавления данных в таблицу "Employer"
            sql_query = "INSERT INTO Employer (Name, Adress, Telephone, Mail, Surname_person, Name_person, date_start) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (rabot_name, address, phone_number, email, responsible_surname, responsible_name, date_start))

            # Выполнение коммита, чтобы сохранить изменения
            connection.commit()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()


    def saveVacancyData(self):
        if (self.VacTitleEdit.text() and self.SalaryEdit.text() and self.ExperienceEdit.text() and 
            self.AdressEdit.text() and self.Level_educationEdit.text() and self.skillsEdit.text() and self.comboBox.currentText()):
            vacancy_title = self.VacTitleEdit.text()
            salary = self.SalaryEdit.text()
            experience = self.ExperienceEdit.text()
            address = self.AdressEdit.text()
            education_level = self.Level_educationEdit.text()
            skills = self.skillsEdit.text()
            
            # Extracting the employer id from the selected combobox item
            employer_id = int(self.comboBox.currentText().split()[0])  # Extracting the ID from the selected item

            status = 'Новая'
            date_public = datetime.datetime.now().date()

            cursor = connection.cursor()

            sql_query = "INSERT INTO Vacancy (title, salary, experience, adress, education, skills, status, date_public, employer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (vacancy_title, salary, experience, address, education_level, skills, status, date_public, employer_id))

            connection.commit()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()





    def clearFields(self):
        self.RabotNameEdit.setText("")  # Сбросить текст в поле для наименования
        self.AdressRabEdit.setText("")   # Сбросить текст в поле для адреса
        self.PhoneNumberEdit.setText("") # Сбросить текст в поле для телефона
        self.MailEdit.setText("")        # Сбросить текст в поле для почты
        self.Name_edit.setText("")
        self.Surname_edit.setText("")       # Сбросить текст в поле для ответственного лица

    def clear_applicant(self):
        self.VacTitleEdit.setText("")    # Сбросить текст в поле для наименования вакансии
        self.SalaryEdit.setText("")      # Сбросить текст в поле для зарплаты
        self.ExperienceEdit.setText("")  # Сбросить текст в поле для требуемого опыта
        self.AdressEdit.setText("")      # Сбросить текст в поле для адреса
        self.Level_educationEdit.setText("")  # Сбросить текст в поле для уровня образования
        self.skillsEdit.setText("")      # Сбросить текст в поле для необходимых навыков



    def BackToMainWindow(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VacWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def retranslateUi(self, Vac_loading):
        _translate = QtCore.QCoreApplication.translate
        Vac_loading.setWindowTitle(_translate("Vac_loading", "Загрузка вакансии"))
        self.label.setText(_translate("Vac_loading", "Загрузка вакансии"))
        self.BackButton.setText(_translate("Vac_loading", "Назад"))
        self.label_5.setText(_translate("Vac_loading", "Вакансия"))
        self.publishButton.setText(_translate("Vac_loading", "Опубликовать"))
        self.label_2.setText(_translate("Vac_loading", "Работодатель"))
        self.label_3.setText(_translate("Vac_loading", "Выбрать из ранее занесённых"))
        self.ClearButton.setText(_translate("Vac_loading", "Очистить"))
        self.SaveButton.setText(_translate("Vac_loading", "Сохранить"))
        self.label_6.setText(_translate("Vac_loading", "Ответственное лицо"))
        self.label_4.setText(_translate("Vac_loading", "или"))
        self.AddSois.setText(_translate("Vac_loading", "Создать нового"))
        self.ClearVac_Button.setText(_translate("Vac_loading", "Очистить"))



        self.RabotNameEdit.setPlaceholderText("Наименование работодателя")
        self.AdressRabEdit.setPlaceholderText("Адрес работодателя")
        self.PhoneNumberEdit.setPlaceholderText("Номер телефона")
        self.MailEdit.setPlaceholderText("Адрес электронной почты")
        self.Surname_edit.setPlaceholderText("Фамилия ответственного лица")
        self.Name_edit.setPlaceholderText("Имя ответственного лица")
        self.VacTitleEdit.setPlaceholderText("Наименование вакансии")
        self.SalaryEdit.setPlaceholderText("Зарплата")
        self.ExperienceEdit.setPlaceholderText("Опыт работы")
        self.AdressEdit.setPlaceholderText("Адрес работы")
        self.Level_educationEdit.setPlaceholderText("Уровень образования")
        self.skillsEdit.setPlaceholderText("Необходимые навыки")
        self.ChooseSoisBtn.setText(_translate("Vac_loading", "Выбрать из занесённых"))


class Ui_EditVacWindow(object):
    def setupUi(self, EditVacWindow, vacancy_id):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditVacWindow.sizePolicy().hasHeightForWidth())
        EditVacWindow.setSizePolicy(sizePolicy)
        EditVacWindow.showMaximized() 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditVacWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(EditVacWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ClearVac_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ClearVac_Button.setGeometry(QtCore.QRect(840, 730, 291, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearVac_Button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearVac_Button.setIcon(icon1)
        self.ClearVac_Button.setObjectName("ClearVac_Button")
        self.publishButton = QtWidgets.QPushButton(self.centralwidget)
        self.publishButton.setGeometry(QtCore.QRect(1170, 730, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.publishButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.publishButton.setIcon(icon2)
        self.publishButton.setObjectName("publishButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(560, 0, 721, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 10, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 80, 501, 771))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 10, 391, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(50, 111, 391, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(240, 140, 121, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 190, 391, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RabotNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.RabotNameEdit.setText("")
        self.RabotNameEdit.setObjectName("RabotNameEdit")
        self.verticalLayout.addWidget(self.RabotNameEdit)
        self.AdressRabEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AdressRabEdit.setFont(font)
        self.AdressRabEdit.setText("")
        self.AdressRabEdit.setObjectName("AdressRabEdit")
        self.verticalLayout.addWidget(self.AdressRabEdit)
        self.PhoneNumberEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PhoneNumberEdit.setText("")
        self.PhoneNumberEdit.setObjectName("PhoneNumberEdit")
        self.verticalLayout.addWidget(self.PhoneNumberEdit)
        self.MailEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.MailEdit.setText("")
        self.MailEdit.setObjectName("MailEdit")
        self.verticalLayout.addWidget(self.MailEdit)
        self.ClearButton = QtWidgets.QPushButton(self.frame_2)
        self.ClearButton.setGeometry(QtCore.QRect(60, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearButton.setFont(font)
        self.ClearButton.setIcon(icon1)
        self.ClearButton.setObjectName("ClearButton")
        self.SaveButton = QtWidgets.QPushButton(self.frame_2)
        self.SaveButton.setGeometry(QtCore.QRect(260, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveButton.setFont(font)
        self.SaveButton.setIcon(icon2)
        self.SaveButton.setObjectName("SaveButton")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(50, 420, 391, 191))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(60, 10, 261, 31))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(50, 0, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Surname_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Surname_edit.setGeometry(QtCore.QRect(60, 60, 261, 31))
        self.Surname_edit.setObjectName("Surname_edit")
        self.Name_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Name_edit.setGeometry(QtCore.QRect(60, 110, 261, 31))
        self.Name_edit.setObjectName("Name_edit")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(839, 80, 601, 601))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(120, 0, 391, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(119, 70, 391, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VacTitleEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.VacTitleEdit.setText("")
        self.VacTitleEdit.setObjectName("VacTitleEdit")
        self.verticalLayout_2.addWidget(self.VacTitleEdit)
        self.SalaryEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SalaryEdit.setText("")
        self.SalaryEdit.setObjectName("SalaryEdit")
        self.verticalLayout_2.addWidget(self.SalaryEdit)
        self.ExperienceEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ExperienceEdit.setText("")
        self.ExperienceEdit.setObjectName("ExperienceEdit")
        self.verticalLayout_2.addWidget(self.ExperienceEdit)
        self.AdressEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.AdressEdit.setText("")
        self.AdressEdit.setObjectName("AdressEdit")
        self.verticalLayout_2.addWidget(self.AdressEdit)
        self.Level_educationEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Level_educationEdit.setText("")
        self.Level_educationEdit.setObjectName("Level_educationEdit")
        self.verticalLayout_2.addWidget(self.Level_educationEdit)
        self.skillsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.skillsEdit.setText("")
        self.skillsEdit.setObjectName("skillsEdit")
        self.verticalLayout_2.addWidget(self.skillsEdit)
        self.Status = QtWidgets.QComboBox(self.frame_4)
        self.Status.setGeometry(QtCore.QRect(210, 440, 201, 71))
        self.Status.setObjectName("Status")
        self.Status.addItems(["Новая", "Неактивная", "Активная", "Закрытая"])
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1770, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon3)
        self.BackButton.setObjectName("BackButton")

        self.AddSois = QtWidgets.QPushButton(self.frame_2)
        self.AddSois.setGeometry(QtCore.QRect(160, 160, 171, 28))
        self.AddSois.setObjectName("AddSois")

        self.ChooseSoisBtn = QtWidgets.QPushButton(self.frame_2)
        self.ChooseSoisBtn.setGeometry(QtCore.QRect(160, 110, 171, 28))
        self.ChooseSoisBtn.setObjectName("ChooseSoisBtn")

        EditVacWindow.setCentralWidget(self.centralwidget)

        self.RabotNameEdit.setToolTip("Наименование работодателя")
        self.AdressRabEdit.setToolTip("Адрес работодателя")
        self.PhoneNumberEdit.setToolTip("Номер телефона")
        self.MailEdit.setToolTip("Адрес электронной почты")
        self.Surname_edit.setToolTip("Фамилия ответственного лица")
        self.Name_edit.setToolTip("Имя ответственного лица")
        self.VacTitleEdit.setToolTip("Наименование вакансии")
        self.SalaryEdit.setToolTip("Зарплата")
        self.ExperienceEdit.setToolTip("Опыт работы")
        self.AdressEdit.setToolTip("Адрес работы")
        self.Level_educationEdit.setToolTip("Уровень образования")
        self.skillsEdit.setToolTip("Необходимые навыки")


        self.retranslateUi(EditVacWindow)
        QtCore.QMetaObject.connectSlotsByName(EditVacWindow)
        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(EditVacWindow))
        self.ClearButton.clicked.connect(self.clearFields)
        self.ClearVac_Button.clicked.connect(self.clear_applicant)
        
        
        self.AddSois.clicked.connect(self.showFields)
        self.ChooseSoisBtn.clicked.connect(self.showCombo)

        self.showCombo()

        cursor = connection.cursor()
        query = "SELECT title, salary, experience, adress, education, skills, status, employer FROM Vacancy WHERE id = %s"
        cursor.execute(query, (vacancy_id,))
        vacancy_info = cursor.fetchone()

        if vacancy_info:
            title, salary, experience, address, education, skills, status, employer = vacancy_info  # Unpack the retrieved values

            # Populate the input fields with the retrieved information
            self.VacTitleEdit.setText(str(vacancy_info['title']))
            self.SalaryEdit.setText(str(vacancy_info['salary']))
            self.ExperienceEdit.setText(str(vacancy_info['experience']))
            self.AdressEdit.setText(str(vacancy_info['adress']))
            self.Level_educationEdit.setText(str(vacancy_info['education']))
            self.skillsEdit.setText(str(vacancy_info['skills']))

            # Assuming Status is a ComboBox
            index = self.Status.findText(status, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.Status.setCurrentIndex(index)
            else:
                # Handle the case where the status is not found in the ComboBox
                # For example, show a default option or display an error message to the user
                self.Status.setCurrentIndex(0)
        else:
            # Handle the case where no vacancy is found for the given ID
            # For example, clear the input fields or show an error message to the user
            self.VacTitleEdit.setText("")
            self.SalaryEdit.setText("")
            self.ExperienceEdit.setText("")
            self.AdressEdit.setText("")
            self.Level_educationEdit.setText("")
            self.skillsEdit.setText("")
            self.Status.setCurrentIndex(0)  # Assuming index 0 represents a default/empty status

        self.fill_employer_combobox(vacancy_info['employer'])
        self.SaveButton.clicked.connect(self.saveEmployerData)
        self.publishButton.clicked.connect(lambda: self.saveVacancyData(vacancy_id,vacancy_info['employer'], EditVacWindow))

    def fill_employer_combobox(self, selected_employer_id):
        cursor = connection.cursor()
        sql_query = "SELECT id, name FROM Employer"  # Query to retrieve employer id and names
        cursor.execute(sql_query)  # Execute the query
        result_set = cursor.fetchall()  # Retrieve the query result
        connection.commit()

        # Clear the combobox to avoid duplicate entries
        self.comboBox.clear()

        # Add employer id and names to the combobox
        for row in result_set:
            employer_id = row['id']
            employer_name = row['name']
            self.comboBox.addItem(f"{employer_id} - {employer_name}")  # Adding both id and name together as an item

            # Select the corresponding employer in the combobox
            if employer_id == selected_employer_id:
                index = self.comboBox.findText(f"{employer_id} - {employer_name}", QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.comboBox.setCurrentIndex(index)




    def showFields(self):
        self.RabotNameEdit.setHidden(False)
        self.AdressRabEdit.setHidden(False)
        self.PhoneNumberEdit.setHidden(False)
        self.MailEdit.setHidden(False)
        self.Surname_edit.setHidden(False)
        self.Name_edit.setHidden(False)
        self.SaveButton.setHidden(False)
        self.ClearButton.setHidden(False)
        self.AddSois.setHidden(True)
        self.frame_6.setHidden(False)
        self.frame_7.setHidden(False)
        self.label_6.setHidden(False)
        self.comboBox.setHidden(True)
        self.label_3.setHidden(True)
        self.ChooseSoisBtn.setHidden(False)

    def showCombo(self):
        self.RabotNameEdit.setHidden(True)
        self.AdressRabEdit.setHidden(True)
        self.PhoneNumberEdit.setHidden(True)
        self.MailEdit.setHidden(True)
        self.Surname_edit.setHidden(True)
        self.Name_edit.setHidden(True)
        self.SaveButton.setHidden(True)
        self.ClearButton.setHidden(True)
        self.AddSois.setHidden(False)
        self.frame_6.setHidden(True)
        self.frame_7.setHidden(True)
        self.label_6.setHidden(True)
        self.comboBox.setHidden(False)
        self.label_3.setHidden(False)
        self.ChooseSoisBtn.setHidden(True)


    def saveEmployerData(self):
        if (self.RabotNameEdit.text() and self.AdressRabEdit.text() and self.PhoneNumberEdit.text() 
        and self.MailEdit.text() and self.Surname_edit.text() and self.Name_edit.text()):

            # Получение введенных пользователем данных
            rabot_name = self.RabotNameEdit.text()
            address = self.AdressRabEdit.text()
            phone_number = self.PhoneNumberEdit.text()
            email = self.MailEdit.text()
            responsible_surname = self.Surname_edit.text()
            responsible_name = self.Name_edit.text()

            # Получение текущей даты
            date_start = datetime.datetime.now().date()

            # Подключение к базе данных
            cursor = connection.cursor()

            # Создание SQL-запроса для добавления данных в таблицу "Employer"
            sql_query = "INSERT INTO Employer (Name, Adress, Telephone, Mail, Surname_person, Name_person, date_start) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (rabot_name, address, phone_number, email, responsible_surname, responsible_name, date_start))

            # Выполнение коммита, чтобы сохранить изменения
            connection.commit()


        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()


    def saveVacancyData(self, vacancy_id, selected_employer_id, EditVacWindow):
        if (self.VacTitleEdit.text() and self.SalaryEdit.text() and self.ExperienceEdit.text() and 
            self.AdressEdit.text() and self.Level_educationEdit.text() and self.skillsEdit.text()):
            # Getting the user-entered data
            vacancy_title = self.VacTitleEdit.text()
            salary = self.SalaryEdit.text()
            experience = self.ExperienceEdit.text()
            address = self.AdressEdit.text()
            education_level = self.Level_educationEdit.text()
            skills = self.skillsEdit.text()
            status = self.Status.currentText()  # Get the selected status from the combo box

            cursor = connection.cursor()

            # Creating SQL query to update data in the "Vacancy" table
            sql_query = "UPDATE Vacancy SET title = %s, salary = %s, experience = %s, adress = %s, education = %s, skills = %s, status = %s, employer = %s WHERE id = %s"
            cursor.execute(sql_query, (vacancy_title, salary, experience, address, education_level, skills, status,selected_employer_id, vacancy_id))

            # Executing the query to update the record
            connection.commit()

            self.BackToMainWindow(EditVacWindow)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Внимание!")
            msg.setText("Заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()



    def clearFields(self):
        self.RabotNameEdit.setText("")  # Сбросить текст в поле для наименования
        self.AdressRabEdit.setText("")   # Сбросить текст в поле для адреса
        self.PhoneNumberEdit.setText("") # Сбросить текст в поле для телефона
        self.MailEdit.setText("")        # Сбросить текст в поле для почты
        self.Name_edit.setText("")
        self.Surname_edit.setText("")       # Сбросить текст в поле для ответственного лица

    def clear_applicant(self):
        self.VacTitleEdit.setText("")    # Сбросить текст в поле для наименования вакансии
        self.SalaryEdit.setText("")      # Сбросить текст в поле для зарплаты
        self.ExperienceEdit.setText("")  # Сбросить текст в поле для требуемого опыта
        self.AdressEdit.setText("")      # Сбросить текст в поле для адреса
        self.Level_educationEdit.setText("")  # Сбросить текст в поле для уровня образования
        self.skillsEdit.setText("") 

    def BackToMainWindow(self, EditVacWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VacWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        EditVacWindow.close()

    def retranslateUi(self, EditVacWindow):
        _translate = QtCore.QCoreApplication.translate
        EditVacWindow.setWindowTitle(_translate("EditVacWindow", "Редактирование вакансии"))
        self.ClearVac_Button.setText(_translate("EditVacWindow", "Очистить"))
        self.publishButton.setText(_translate("EditVacWindow", "Опубликовать"))
        self.label.setText(_translate("EditVacWindow", "Редактирование вакансии"))
        self.label_2.setText(_translate("EditVacWindow", "Работодатель"))
        self.label_3.setText(_translate("EditVacWindow", "Выбрать из ранее занесённых"))
        self.label_4.setText(_translate("EditVacWindow", "или"))
        self.ClearButton.setText(_translate("EditVacWindow", "Очистить"))
        self.SaveButton.setText(_translate("EditVacWindow", "Сохранить"))
        self.label_6.setText(_translate("EditVacWindow", "Ответственное лицо"))
        self.label_5.setText(_translate("EditVacWindow", "Вакансия"))
        self.BackButton.setText(_translate("EditVacWindow", "Назад"))
        self.ChooseSoisBtn.setText(_translate("EditVacWindow", "Выбрать из занесённых"))
        self.AddSois.setText(_translate("EditVacWindow", "Создать нового"))

        self.RabotNameEdit.setPlaceholderText("Наименование работодателя")
        self.AdressRabEdit.setPlaceholderText("Адрес работодателя")
        self.PhoneNumberEdit.setPlaceholderText("Номер телефона")
        self.MailEdit.setPlaceholderText("Адрес электронной почты")
        self.Surname_edit.setPlaceholderText("Фамилия ответственного лица")
        self.Name_edit.setPlaceholderText("Имя ответственного лица")
        self.VacTitleEdit.setPlaceholderText("Наименование вакансии")
        self.SalaryEdit.setPlaceholderText("Зарплата")
        self.ExperienceEdit.setPlaceholderText("Опыт работы")
        self.AdressEdit.setPlaceholderText("Адрес работы")
        self.Level_educationEdit.setPlaceholderText("Уровень образования")
        self.skillsEdit.setPlaceholderText("Необходимые навыки")

class Ui_Rab_loading(object):
    def setupUi(self, Vac_loading):
        Vac_loading.setObjectName("Vac_loading")
        Vac_loading.resize(1920, 1015)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vac_loading.sizePolicy().hasHeightForWidth())
        Vac_loading.setSizePolicy(sizePolicy)
        Vac_loading.showMaximized() 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Vac_loading.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Vac_loading)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(590, 0, 721, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(590, 80, 721, 891))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 10, 621, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ClearButton = QtWidgets.QPushButton(self.frame_2)
        self.ClearButton.setGeometry(QtCore.QRect(20, 680, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon1)
        self.ClearButton.setObjectName("ClearButton")
        self.SaveButton = QtWidgets.QPushButton(self.frame_2)
        self.SaveButton.setGeometry(QtCore.QRect(460, 680, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveButton.setIcon(icon2)
        self.SaveButton.setObjectName("SaveButton")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(140, 400, 441, 191))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(90, 10, 261, 31))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(50, 0, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Surname_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Surname_edit.setGeometry(QtCore.QRect(90, 60, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Surname_edit.setFont(font)
        self.Surname_edit.setObjectName("Surname_edit")
        self.Name_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Name_edit.setGeometry(QtCore.QRect(90, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_edit.setFont(font)
        self.Name_edit.setObjectName("Name_edit")
        self.RabotNameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.RabotNameEdit.setGeometry(QtCore.QRect(140, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RabotNameEdit.setFont(font)
        self.RabotNameEdit.setText("")
        self.RabotNameEdit.setObjectName("RabotNameEdit")
        self.AdressRabEdit = QtWidgets.QLineEdit(self.frame_2)
        self.AdressRabEdit.setGeometry(QtCore.QRect(140, 170, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AdressRabEdit.setFont(font)
        self.AdressRabEdit.setText("")
        self.AdressRabEdit.setObjectName("AdressRabEdit")
        self.PhoneNumberEdit = QtWidgets.QLineEdit(self.frame_2)
        self.PhoneNumberEdit.setGeometry(QtCore.QRect(140, 230, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PhoneNumberEdit.setFont(font)
        self.PhoneNumberEdit.setText("")
        self.PhoneNumberEdit.setObjectName("PhoneNumberEdit")
        self.MailEdit = QtWidgets.QLineEdit(self.frame_2)
        self.MailEdit.setGeometry(QtCore.QRect(140, 300, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MailEdit.setFont(font)
        self.MailEdit.setText("")
        self.MailEdit.setObjectName("MailEdit")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1770, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon3)
        self.BackButton.setObjectName("BackButton")
        Vac_loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(Vac_loading)
        QtCore.QMetaObject.connectSlotsByName(Vac_loading)

        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(Vac_loading))
        self.ClearButton.clicked.connect(self.clearFields)
        self.SaveButton.clicked.connect(lambda: self.saveEmployerData(Vac_loading))


        self.RabotNameEdit.setToolTip("Наименование работодателя")
        self.AdressRabEdit.setToolTip("Адрес работодателя")
        self.PhoneNumberEdit.setToolTip("Номер телефона")
        self.MailEdit.setToolTip("Адрес электронной почты")
        self.Surname_edit.setToolTip("Фамилия ответственного лица")
        self.Name_edit.setToolTip("Имя ответственного лица")


    def saveEmployerData(self, Vac_loading):
        if (self.RabotNameEdit.text() and self.AdressRabEdit.text() and self.PhoneNumberEdit.text() 
        and self.MailEdit.text() and self.Surname_edit.text() and self.Name_edit.text()):

            # Получение введенных пользователем данных
            rabot_name = self.RabotNameEdit.text()
            address = self.AdressRabEdit.text()
            phone_number = self.PhoneNumberEdit.text()
            email = self.MailEdit.text()
            responsible_surname = self.Surname_edit.text()
            responsible_name = self.Name_edit.text()

            # Получение текущей даты
            date_start = datetime.datetime.now().date()

            # Подключение к базе данных
            cursor = connection.cursor()

            # Создание SQL-запроса для добавления данных в таблицу "Employer"
            sql_query = "INSERT INTO Employer (Name, Adress, Telephone, Mail, Surname_person, Name_person, date_start) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (rabot_name, address, phone_number, email, responsible_surname, responsible_name, date_start))

            # Выполнение коммита, чтобы сохранить изменения
            connection.commit()

            self.BackToMainWindow(Vac_loading)

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def clearFields(self):
        self.RabotNameEdit.setText("")  # Сбросить текст в поле для наименования
        self.AdressRabEdit.setText("")   # Сбросить текст в поле для адреса
        self.PhoneNumberEdit.setText("") # Сбросить текст в поле для телефона
        self.MailEdit.setText("")        # Сбросить текст в поле для почты
        self.Name_edit.setText("")
        self.Surname_edit.setText("")       # Сбросить текст в поле для ответственного лица


    def BackToMainWindow(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RabotWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def retranslateUi(self, Vac_loading):
        _translate = QtCore.QCoreApplication.translate
        Vac_loading.setWindowTitle(_translate("Vac_loading", "Загрузка работодателя"))
        self.label.setText(_translate("Vac_loading", "Загрузка работодателя"))
        self.BackButton.setText(_translate("Vac_loading", "Назад"))
        self.label_2.setText(_translate("Vac_loading", "Работодатель"))
        self.ClearButton.setText(_translate("Vac_loading", "Очистить"))
        self.SaveButton.setText(_translate("Vac_loading", "Сохранить"))
        self.label_6.setText(_translate("Vac_loading", "Ответственное лицо"))

        self.RabotNameEdit.setPlaceholderText("Наименование работодателя")
        self.AdressRabEdit.setPlaceholderText("Адрес работодателя")
        self.PhoneNumberEdit.setPlaceholderText("Номер телефона")
        self.MailEdit.setPlaceholderText("Адрес электронной почты")
        self.Surname_edit.setPlaceholderText("Фамилия ответственного лица")
        self.Name_edit.setPlaceholderText("Имя ответственного лица")

class Ui_Rab_edit(object):
    def setupUi(self, Vac_loading, employer_id):
        Vac_loading.setObjectName("Vac_loading")
        Vac_loading.resize(1920, 1015)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vac_loading.sizePolicy().hasHeightForWidth())
        Vac_loading.setSizePolicy(sizePolicy)
        Vac_loading.showMaximized() 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Vac_loading.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Vac_loading)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(590, 0, 721, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(590, 80, 721, 891))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 10, 621, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ClearButton = QtWidgets.QPushButton(self.frame_2)
        self.ClearButton.setGeometry(QtCore.QRect(20, 680, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClearButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon1)
        self.ClearButton.setObjectName("ClearButton")
        self.SaveButton = QtWidgets.QPushButton(self.frame_2)
        self.SaveButton.setGeometry(QtCore.QRect(460, 680, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveButton.setIcon(icon2)
        self.SaveButton.setObjectName("SaveButton")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(140, 400, 441, 191))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(90, 10, 261, 31))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(50, 0, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Surname_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Surname_edit.setGeometry(QtCore.QRect(90, 60, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Surname_edit.setFont(font)
        self.Surname_edit.setObjectName("Surname_edit")
        self.Name_edit = QtWidgets.QLineEdit(self.frame_6)
        self.Name_edit.setGeometry(QtCore.QRect(90, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_edit.setFont(font)
        self.Name_edit.setObjectName("Name_edit")
        self.RabotNameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.RabotNameEdit.setGeometry(QtCore.QRect(140, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RabotNameEdit.setFont(font)
        self.RabotNameEdit.setText("")
        self.RabotNameEdit.setObjectName("RabotNameEdit")
        self.AdressRabEdit = QtWidgets.QLineEdit(self.frame_2)
        self.AdressRabEdit.setGeometry(QtCore.QRect(140, 170, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AdressRabEdit.setFont(font)
        self.AdressRabEdit.setText("")
        self.AdressRabEdit.setObjectName("AdressRabEdit")
        self.PhoneNumberEdit = QtWidgets.QLineEdit(self.frame_2)
        self.PhoneNumberEdit.setGeometry(QtCore.QRect(140, 230, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PhoneNumberEdit.setFont(font)
        self.PhoneNumberEdit.setText("")
        self.PhoneNumberEdit.setObjectName("PhoneNumberEdit")
        self.MailEdit = QtWidgets.QLineEdit(self.frame_2)
        self.MailEdit.setGeometry(QtCore.QRect(140, 300, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MailEdit.setFont(font)
        self.MailEdit.setText("")
        self.MailEdit.setObjectName("MailEdit")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1770, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon3)
        self.BackButton.setObjectName("BackButton")
        Vac_loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(Vac_loading)
        QtCore.QMetaObject.connectSlotsByName(Vac_loading)

        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(Vac_loading))
        self.ClearButton.clicked.connect(self.clearFields)
        


        self.RabotNameEdit.setToolTip("Наименование работодателя")
        self.AdressRabEdit.setToolTip("Адрес работодателя")
        self.PhoneNumberEdit.setToolTip("Номер телефона")
        self.MailEdit.setToolTip("Адрес электронной почты")
        self.Surname_edit.setToolTip("Фамилия ответственного лица")
        self.Name_edit.setToolTip("Имя ответственного лица")

        cursor = connection.cursor()
        query = "SELECT name, adress, telephone, mail, surname_person, name_person FROM Employer WHERE id = %s"
        cursor.execute(query, (employer_id,))
        employer_info = cursor.fetchone()

        if employer_info:
            # Populate the input fields with the retrieved information
            self.RabotNameEdit.setText(str(employer_info['name']))
            self.AdressRabEdit.setText(str(employer_info['adress']))
            self.PhoneNumberEdit.setText(str(employer_info['telephone']))
            self.MailEdit.setText(str(employer_info['mail']))
            self.Surname_edit.setText(str(employer_info['surname_person']))
            self.Name_edit.setText(str(employer_info['name_person']))


        else:
            # Handle the case where no vacancy is found for the given ID
            # For example, clear the input fields or show an error message to the user
            self.RabotNameEdit.setText("")
            self.AdressRabEdit.setText("")
            self.PhoneNumberEdit.setText("")
            self.MailEdit.setText("")
            self.Surname_edit.setText("")
            self.Name_edit.setText("")

        self.SaveButton.clicked.connect(lambda: self.saveEmployerData(employer_id, Vac_loading))

    def saveEmployerData(self, employer_id, Vac_loading):
        if (self.RabotNameEdit.text() and self.AdressRabEdit.text() and self.PhoneNumberEdit.text() 
        and self.MailEdit.text() and self.Surname_edit.text() and self.Name_edit.text()):

            # Получение введенных пользователем данных
            rabot_name = self.RabotNameEdit.text()
            address = self.AdressRabEdit.text()
            phone_number = self.PhoneNumberEdit.text()
            email = self.MailEdit.text()
            responsible_surname = self.Surname_edit.text()
            responsible_name = self.Name_edit.text()

            # Получение текущей даты
            date_start = datetime.datetime.now().date()

            # Подключение к базе данных
            cursor = connection.cursor()

            # Создание SQL-запроса для добавления данных в таблицу "Employer"
            sql_query = "UPDATE Employer SET Name = %s, Adress = %s, Telephone = %s, Mail = %s, Surname_person = %s, Name_person = %s, date_start = %s WHERE id = %s"
            cursor.execute(sql_query, (rabot_name, address, phone_number, email, responsible_surname, responsible_name, date_start, employer_id))


            # Выполнение коммита, чтобы сохранить изменения
            connection.commit()
            self.BackToMainWindow(Vac_loading)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def clearFields(self):
        self.RabotNameEdit.setText("")  # Сбросить текст в поле для наименования
        self.AdressRabEdit.setText("")   # Сбросить текст в поле для адреса
        self.PhoneNumberEdit.setText("") # Сбросить текст в поле для телефона
        self.MailEdit.setText("")        # Сбросить текст в поле для почты
        self.Name_edit.setText("")
        self.Surname_edit.setText("")       # Сбросить текст в поле для ответственного лица


    def BackToMainWindow(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RabotWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def retranslateUi(self, Vac_loading):
        _translate = QtCore.QCoreApplication.translate
        Vac_loading.setWindowTitle(_translate("Vac_loading", "Редактирование работодателя"))
        self.label.setText(_translate("Vac_loading", "Редактирование работодателя"))
        self.BackButton.setText(_translate("Vac_loading", "Назад"))
        self.label_2.setText(_translate("Vac_loading", "Работодатель"))
        self.ClearButton.setText(_translate("Vac_loading", "Очистить"))
        self.SaveButton.setText(_translate("Vac_loading", "Сохранить"))
        self.label_6.setText(_translate("Vac_loading", "Ответственное лицо"))

        self.RabotNameEdit.setPlaceholderText("Наименование работодателя")
        self.AdressRabEdit.setPlaceholderText("Адрес работодателя")
        self.PhoneNumberEdit.setPlaceholderText("Номер телефона")
        self.MailEdit.setPlaceholderText("Адрес электронной почты")
        self.Surname_edit.setPlaceholderText("Фамилия ответственного лица")
        self.Name_edit.setPlaceholderText("Имя ответственного лица")


        
class Ui_load_ankets(object):
    def setupUi(self, load_ankets):
        load_ankets.setObjectName("load_ankets")
        load_ankets.setWindowModality(QtCore.Qt.NonModal)
        load_ankets.setEnabled(True)
        load_ankets.showMaximized()  # Открыть окно на весь экран

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(load_ankets.sizePolicy().hasHeightForWidth())
        load_ankets.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        load_ankets.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(load_ankets)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(640, 0, 761, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(70, 50, 701, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(210, 10, 301, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 120, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 180, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 240, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 240, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(780, 50, 1061, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.NoExpButton = QtWidgets.QPushButton(self.frame_3)
        self.NoExpButton.setGeometry(QtCore.QRect(810, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NoExpButton.setFont(font)
        self.NoExpButton.setObjectName("NoExpButton")
        self.Year_of_expEdit = QtWidgets.QLineEdit(self.frame_3)
        self.Year_of_expEdit.setGeometry(QtCore.QRect(20, 90, 341, 41))
        self.Year_of_expEdit.setObjectName("Year_of_expEdit")
        self.Place_expEdit = QtWidgets.QLineEdit(self.frame_3)
        self.Place_expEdit.setGeometry(QtCore.QRect(370, 90, 671, 41))
        self.Place_expEdit.setObjectName("Place_expEdit")
        self.Plus_ExpButton = QtWidgets.QPushButton(self.frame_3)
        self.Plus_ExpButton.setGeometry(QtCore.QRect(20, 40, 51, 41))
        self.Plus_ExpButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Plus_ExpButton.setIcon(icon1)
        self.Plus_ExpButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_ExpButton.setObjectName("Plus_ExpButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(780, 210, 1061, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setGeometry(QtCore.QRect(90, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Place_eduEdit = QtWidgets.QLineEdit(self.frame_4)
        self.Place_eduEdit.setGeometry(QtCore.QRect(250, 90, 361, 41))
        self.Place_eduEdit.setObjectName("Place_eduEdit")
        self.Year_of_educEdit = QtWidgets.QLineEdit(self.frame_4)
        self.Year_of_educEdit.setGeometry(QtCore.QRect(10, 90, 231, 41))
        self.Year_of_educEdit.setObjectName("Year_of_educEdit")
        self.Plus_EducButton = QtWidgets.QPushButton(self.frame_4)
        self.Plus_EducButton.setGeometry(QtCore.QRect(20, 40, 51, 41))
        self.Plus_EducButton.setText("")
        self.Plus_EducButton.setIcon(icon1)
        self.Plus_EducButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_EducButton.setObjectName("Plus_EducButton")
        self.SpecialEdit = QtWidgets.QLineEdit(self.frame_4)
        self.SpecialEdit.setGeometry(QtCore.QRect(620, 90, 421, 41))
        self.SpecialEdit.setObjectName("SpecialEdit")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(780, 380, 1061, 311))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setGeometry(QtCore.QRect(110, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 80, 851, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.Plus_SkillsButton = QtWidgets.QPushButton(self.frame_5)
        self.Plus_SkillsButton.setGeometry(QtCore.QRect(20, 80, 51, 41))
        self.Plus_SkillsButton.setText("")
        self.Plus_SkillsButton.setIcon(icon1)
        self.Plus_SkillsButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_SkillsButton.setObjectName("Plus_SkillsButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(780, 760, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ExitButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/NO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon2)
        self.ExitButton.setObjectName("ExitButton")
        self.loadingButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadingButton.setGeometry(QtCore.QRect(1340, 760, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadingButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadingButton.setIcon(icon3)
        self.loadingButton.setObjectName("loadingButton")
        self.Resume_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_btn.setGeometry(QtCore.QRect(70, 440, 181, 151))
        self.Resume_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/Resume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Resume_btn.setIcon(icon4)
        self.Resume_btn.setIconSize(QtCore.QSize(100, 100))
        self.Resume_btn.setObjectName("Resume_btn")
        self.Resume_btn.setHidden(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 590, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        load_ankets.setCentralWidget(self.centralwidget)
        self.NoSkillButton = QtWidgets.QPushButton(self.frame_5)
        self.NoSkillButton.setGeometry(QtCore.QRect(800, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NoSkillButton.setFont(font)
        self.NoEduButton = QtWidgets.QPushButton(self.frame_4)
        self.NoEduButton.setGeometry(QtCore.QRect(810, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NoEduButton.setFont(font)
        self.NoEduButton.setObjectName("NoEduButton")

        self.retranslateUi(load_ankets)
        QtCore.QMetaObject.connectSlotsByName(load_ankets)

        self.ExitButton.clicked.connect(lambda: self.BackToMainWindow(load_ankets))
        self.loadingButton.clicked.connect(lambda:self.click_on_loadingButton(load_ankets))

        date_mask = '0000-00-00'
        self.lineEdit_3.setInputMask(date_mask)


        self.Year_of_educEdit.setToolTip('Годы обучения')
        self.Year_of_expEdit.setToolTip('Опыт работы')
        self.Place_eduEdit.setToolTip('Место обучения')
        self.Place_expEdit.setToolTip('Место работы')
        self.SpecialEdit.setToolTip('Специальность')
        self.lineEdit.setToolTip('Имя')
        self.lineEdit_2.setToolTip('Фамилия')
        self.lineEdit_3.setToolTip('Дата рождения')
        self.lineEdit_4.setToolTip('Номер телефона')
        self.lineEdit_5.setToolTip('Почта')
        self.lineEdit_6.setToolTip('Город проживания')

        self.Plus_EducButton.setHidden(True)
        self.Plus_ExpButton.setHidden(True)
        self.Plus_SkillsButton.setHidden(True)
            # Привязка обработчика события нажатия на кнопку "Нет опыта"
        self.NoExpButton.clicked.connect(self.hideExperienceFields)
        self.Plus_ExpButton.clicked.connect(self.showExperienceFields)

        self.NoEduButton.clicked.connect(self.hideEduFields)
        self.Plus_EducButton.clicked.connect(self.showEduFields)

        self.NoSkillButton.clicked.connect(self.hideSkillFields)
        self.Plus_SkillsButton.clicked.connect(self.showSkillFields)
        # Функция для скрытия элементов при нажатии на кнопку "Нет опыта"
    def hideExperienceFields(self):
        self.Place_expEdit.setHidden(True)  # Скрыть поле "Место работы"
        self.Year_of_expEdit.setHidden(True)
        self.Plus_ExpButton.setHidden(False)  # Скрыть поле "Опыт работы"

    def showExperienceFields(self):
        self.Place_expEdit.setHidden(False)  # показать поле "Место работы"
        self.Year_of_expEdit.setHidden(False)
        self.Plus_ExpButton.setHidden(True)  # показать поле "Опыт работы"

    def hideEduFields(self):
        self.Place_eduEdit.setHidden(True) 
        self.SpecialEdit.setHidden(True)
        self.Year_of_educEdit.setHidden(True)
        self.Plus_EducButton.setHidden(False) 

    def showEduFields(self):
        self.Place_eduEdit.setHidden(False)
        self.SpecialEdit.setHidden(False) 
        self.Year_of_educEdit.setHidden(False)
        self.Plus_EducButton.setHidden(True) 


    def hideSkillFields(self):
        self.lineEdit_7.setHidden(True) 
        self.Plus_SkillsButton.setHidden(False) 

    def showSkillFields(self):
        self.lineEdit_7.setHidden(False) 
        self.Plus_SkillsButton.setHidden(True) 

    def BackToMainWindow(self, load_ankets):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SoiscWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        load_ankets.close()

    def click_on_loadingButton (self, load_ankets):
        cursor = connection.cursor()

        # Получение данных из полей ввода (замените на соответствующие переменные в вашем коде)
        year_of_educ = self.Year_of_educEdit.text()
        year_of_exp = self.Year_of_expEdit.text()
        place_edu = self.Place_eduEdit.text()
        place_exp = self.Place_expEdit.text()
        specialty = self.SpecialEdit.text()
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        birth_date = self.lineEdit_3.text()
        phone_number = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        city = self.lineEdit_6.text()
        skills = self.lineEdit_7.text()

        try:
            datetime.datetime.strptime(birth_date, '%Y-%m-%d')  # Пытаемся разобрать введенную дату
        except ValueError:
            # Если дата не соответствует формату, выводим сообщение об ошибке в диалоговом окне
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка в формате даты")
            msg.setInformativeText("Дата рождения имеет неправильный формат. Используйте формат ГГГГ-ММ-ДД.")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        if first_name and last_name and birth_date and phone_number and email and city:
            # Операция INSERT для вставки данных в таблицу Applicant
            insert_query = """INSERT INTO Applicant (Year_educ, Year_ex, Place_educ, Place_ex, Special, name, surname, date_of_birth, telephone, mail, City, skills) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (year_of_educ, year_of_exp, place_edu, place_exp, specialty, first_name, last_name, birth_date, phone_number, email, city, skills)
            cursor.execute(insert_query, data)
            # Подтверждение транзакции и закрытие соединения
            connection.commit()
            self.BackToMainWindow(load_ankets)

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
    def retranslateUi(self, load_ankets):
        _translate = QtCore.QCoreApplication.translate
        load_ankets.setWindowTitle(_translate("load_ankets", "Загрузка анкеты соискателя"))
        self.label.setText(_translate("load_ankets", "Загрузка анкеты соискателя"))
        self.label_3.setText(_translate("load_ankets", "Основная информация"))
        self.lineEdit.setPlaceholderText(_translate("load_ankets", "Имя"))
        self.lineEdit_2.setPlaceholderText(_translate("load_ankets", "Фамилия"))
        self.lineEdit_3.setPlaceholderText(_translate("load_ankets", "Дата рождения"))
        self.lineEdit_4.setPlaceholderText(_translate("load_ankets", "Номер телефона"))
        self.lineEdit_5.setPlaceholderText(_translate("load_ankets", "Почта"))
        self.lineEdit_6.setPlaceholderText(_translate("load_ankets", "Город проживания"))
        self.label_4.setText(_translate("load_ankets", "Опыт работы"))
        self.NoExpButton.setText(_translate("load_ankets", "Нет опыта"))
        self.Year_of_expEdit.setPlaceholderText(_translate("load_ankets", "Годы"))
        self.Place_expEdit.setPlaceholderText(_translate("load_ankets", "Место"))
        self.label_5.setText(_translate("load_ankets", "Образование"))
        self.Place_eduEdit.setPlaceholderText(_translate("load_ankets", "Место"))
        self.Year_of_educEdit.setPlaceholderText(_translate("load_ankets", "Годы"))
        self.SpecialEdit.setPlaceholderText(_translate("load_ankets", "Специализация"))
        self.label_7.setText(_translate("load_ankets", "Навыки"))
        self.ExitButton.setText(_translate("load_ankets", "Отменить заполение и выйти"))
        self.loadingButton.setText(_translate("load_ankets", "Загрузить анкету"))
        self.NoEduButton.setText(_translate("load_ankets", "Нет образования"))
        self.NoSkillButton.setText(_translate("load_ankets", "Навыки не указаны"))


class Ui_edit_anketa_soiscWindow(object):
    def setupUi(self, edit_anketa_soiscWindow, applicant_id):
        edit_anketa_soiscWindow.setObjectName("edit_anketa_soiscWindow")
        edit_anketa_soiscWindow.setWindowModality(QtCore.Qt.NonModal)
        edit_anketa_soiscWindow.setEnabled(True)
        edit_anketa_soiscWindow.showMaximized()  # Открыть окно на весь экран

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_anketa_soiscWindow.sizePolicy().hasHeightForWidth())
        edit_anketa_soiscWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edit_anketa_soiscWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(edit_anketa_soiscWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(560, 0, 761, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 0, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loadingButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadingButton.setGeometry(QtCore.QRect(1390, 800, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadingButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadingButton.setIcon(icon1)
        self.loadingButton.setObjectName("loadingButton")

        self.status = QtWidgets.QComboBox(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(610, 460, 211, 61))
        self.status.setObjectName("status")
        self.status.setStyleSheet("font-size: 14px;")


        status_options = ["Новый", "Просмотрен", "Подходит на вакансию", "Принят на работу"]

        for option in status_options:
            self.status.addItem(option)

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(830, 60, 1061, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.NoExpButton = QtWidgets.QPushButton(self.frame_3)
        self.NoExpButton.setGeometry(QtCore.QRect(810, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NoExpButton.setFont(font)
        self.NoExpButton.setObjectName("NoExpButton")
        self.Year_of_expEdit = QtWidgets.QLineEdit(self.frame_3)
        self.Year_of_expEdit.setGeometry(QtCore.QRect(20, 90, 341, 41))
        self.Year_of_expEdit.setObjectName("Year_of_expEdit")
        self.Place_expEdit = QtWidgets.QLineEdit(self.frame_3)
        self.Place_expEdit.setGeometry(QtCore.QRect(370, 90, 671, 41))
        self.Place_expEdit.setObjectName("Place_expEdit")
        self.Plus_ExpButton = QtWidgets.QPushButton(self.frame_3)
        self.Plus_ExpButton.setGeometry(QtCore.QRect(20, 40, 51, 41))
        self.Plus_ExpButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Plus_ExpButton.setIcon(icon2)
        self.Plus_ExpButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_ExpButton.setObjectName("Plus_ExpButton")
        self.loadingButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.loadingButton_2.setGeometry(QtCore.QRect(2020, 950, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadingButton_2.setFont(font)
        self.loadingButton_2.setIcon(icon1)
        self.loadingButton_2.setObjectName("loadingButton_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(830, 220, 1061, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setGeometry(QtCore.QRect(90, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Place_eduEdit = QtWidgets.QLineEdit(self.frame_4)
        self.Place_eduEdit.setGeometry(QtCore.QRect(250, 90, 361, 41))
        self.Place_eduEdit.setObjectName("Place_eduEdit")
        self.Year_of_educEdit = QtWidgets.QLineEdit(self.frame_4)
        self.Year_of_educEdit.setGeometry(QtCore.QRect(10, 90, 231, 41))
        self.Year_of_educEdit.setObjectName("Year_of_educEdit")
        self.Plus_EducButton = QtWidgets.QPushButton(self.frame_4)
        self.Plus_EducButton.setGeometry(QtCore.QRect(20, 40, 51, 41))
        self.Plus_EducButton.setText("")
        self.Plus_EducButton.setIcon(icon2)
        self.Plus_EducButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_EducButton.setObjectName("Plus_EducButton")
        self.SpecialEdit = QtWidgets.QLineEdit(self.frame_4)
        self.SpecialEdit.setGeometry(QtCore.QRect(620, 90, 421, 41))
        self.SpecialEdit.setObjectName("SpecialEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 610, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(120, 60, 701, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(210, 10, 301, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 120, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 180, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 240, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 240, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(830, 390, 1061, 311))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setGeometry(QtCore.QRect(420, 10, 301, 51))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setGeometry(QtCore.QRect(110, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 80, 851, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.Plus_SkillsButton = QtWidgets.QPushButton(self.frame_5)
        self.Plus_SkillsButton.setGeometry(QtCore.QRect(20, 80, 51, 41))
        self.Plus_SkillsButton.setText("")
        self.Plus_SkillsButton.setIcon(icon2)
        self.Plus_SkillsButton.setIconSize(QtCore.QSize(40, 40))
        self.Plus_SkillsButton.setObjectName("Plus_SkillsButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(830, 800, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ExitButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/NO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon3)
        self.ExitButton.setObjectName("ExitButton")
        self.NoSkillButton = QtWidgets.QPushButton(self.frame_5)
        self.NoSkillButton.setGeometry(QtCore.QRect(800, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NoSkillButton.setFont(font)
        self.NoEduButton = QtWidgets.QPushButton(self.frame_4)
        self.NoEduButton.setGeometry(QtCore.QRect(810, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NoEduButton.setFont(font)
        self.NoEduButton.setObjectName("NoEduButton")
        edit_anketa_soiscWindow.setCentralWidget(self.centralwidget)
        date_mask = '0000-00-00'
        self.lineEdit_3.setInputMask(date_mask)

        self.Plus_EducButton.setHidden(True)
        self.Plus_ExpButton.setHidden(True)
        self.Plus_SkillsButton.setHidden(True)

        self.NoExpButton.clicked.connect(self.hideExperienceFields)
        self.Plus_ExpButton.clicked.connect(self.showExperienceFields)

        self.NoEduButton.clicked.connect(self.hideEduFields)
        self.Plus_EducButton.clicked.connect(self.showEduFields)

        self.NoSkillButton.clicked.connect(self.hideSkillFields)
        self.Plus_SkillsButton.clicked.connect(self.showSkillFields)

        self.retranslateUi(edit_anketa_soiscWindow)
        QtCore.QMetaObject.connectSlotsByName(edit_anketa_soiscWindow)

        self.ExitButton.clicked.connect(lambda: self.BackToMainWindow(edit_anketa_soiscWindow))
        

        self.Year_of_educEdit.setToolTip('Годы обучения')
        self.Year_of_expEdit.setToolTip('Опыт работы')
        self.Place_eduEdit.setToolTip('Место обучения')
        self.Place_expEdit.setToolTip('Место работы')
        self.SpecialEdit.setToolTip('Специальность')
        self.lineEdit.setToolTip('Имя')
        self.lineEdit_2.setToolTip('Фамилия')
        self.lineEdit_3.setToolTip('Дата рождения')
        self.lineEdit_4.setToolTip('Номер телефона')
        self.lineEdit_5.setToolTip('Почта')
        self.lineEdit_6.setToolTip('Город проживания')

        with connection.cursor() as cursor:
            # Получение информации о соискателе из базы данных
            sql_query = "SELECT * FROM Applicant WHERE id = %s"
            cursor.execute(sql_query, (applicant_id,))
            applicant_data = cursor.fetchone()
            applicant_id = applicant_data['id']


            # Заполнение полей интерфейса данными о соискателе
            self.Year_of_educEdit.setText(applicant_data['year_educ'])
            self.Year_of_expEdit.setText(applicant_data['year_ex'])
            self.Place_eduEdit.setText(applicant_data['place_educ'])
            self.Place_expEdit.setText(applicant_data['place_ex'])
            self.SpecialEdit.setText(applicant_data['special'])
            self.lineEdit.setText(applicant_data['name'])
            self.lineEdit_2.setText(applicant_data['surname'])
            self.lineEdit_3.setText(applicant_data['date_of_birth'].strftime('%Y-%m-%d'))
            self.lineEdit_4.setText(applicant_data['telephone'])
            self.lineEdit_5.setText(applicant_data['mail'])
            self.lineEdit_6.setText(applicant_data['city'])

        self.loadingButton.clicked.connect(lambda: self.click_on_loadingButton(edit_anketa_soiscWindow, applicant_id))

    def click_on_loadingButton(self, load_ankets, applicant_id):
        year_of_educ = self.Year_of_educEdit.text()
        year_of_exp = self.Year_of_expEdit.text()
        place_edu = self.Place_eduEdit.text()
        place_exp = self.Place_expEdit.text()
        specialty = self.SpecialEdit.text()
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        birth_date = self.lineEdit_3.text()
        phone_number = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        city = self.lineEdit_6.text()
        skills = self.lineEdit_7.text()
        status = self.status.currentText()  # Get the selected status from the combo box

        try:
            datetime.datetime.strptime(birth_date, '%Y-%m-%d')  # Пытаемся разобрать введенную дату
        except ValueError:
            # Если дата не соответствует формату, выводим сообщение об ошибке в диалоговом окне
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка в формате даты")
            msg.setInformativeText("Дата рождения имеет неправильный формат. Используйте формат ГГГГ-ММ-ДД.")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        if first_name and last_name and birth_date and phone_number and email and city:
            cursor = connection.cursor()
            # Операция UPDATE для обновления данных в таблице Applicant
            update_query = """
                UPDATE Applicant 
                SET Year_educ = %s, 
                    Year_ex = %s, 
                    Place_educ = %s, 
                    Place_ex = %s, 
                    Special = %s, 
                    name = %s, 
                    surname = %s, 
                    date_of_birth = %s, 
                    telephone = %s, 
                    mail = %s, 
                    City = %s,
                    status = %s,  
                    skills = %s
                WHERE id = %s
            """
            data = (year_of_educ, year_of_exp, place_edu, place_exp, specialty, first_name, last_name, birth_date, phone_number, email, city, status, skills, applicant_id)
            cursor.execute(update_query, data)
            # Подтверждение транзакции и закрытие соединения
            connection.commit()
            self.BackToMainWindow(load_ankets)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Пожалуйста, заполните все поля для ввода")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def BackToMainWindow(self, edit_anketa_soiscWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SoiscWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        edit_anketa_soiscWindow.close()

    def hideExperienceFields(self):
        self.Place_expEdit.setHidden(True)  # Скрыть поле "Место работы"
        self.Year_of_expEdit.setHidden(True)
        self.Plus_ExpButton.setHidden(False)  # Скрыть поле "Опыт работы"

    def showExperienceFields(self):
        self.Place_expEdit.setHidden(False)  # показать поле "Место работы"
        self.Year_of_expEdit.setHidden(False)
        self.Plus_ExpButton.setHidden(True)  # показать поле "Опыт работы"

    def hideEduFields(self):
        self.Place_eduEdit.setHidden(True) 
        self.SpecialEdit.setHidden(True)
        self.Year_of_educEdit.setHidden(True)
        self.Plus_EducButton.setHidden(False) 

    def showEduFields(self):
        self.Place_eduEdit.setHidden(False)
        self.SpecialEdit.setHidden(False) 
        self.Year_of_educEdit.setHidden(False)
        self.Plus_EducButton.setHidden(True) 


    def hideSkillFields(self):
        self.lineEdit_7.setHidden(True) 
        self.Plus_SkillsButton.setHidden(False) 

    def showSkillFields(self):
        self.lineEdit_7.setHidden(False) 
        self.Plus_SkillsButton.setHidden(True) 


    def retranslateUi(self, edit_anketa_soiscWindow):
        _translate = QtCore.QCoreApplication.translate
        edit_anketa_soiscWindow.setWindowTitle(_translate("edit_anketa_soiscWindow", "Редактирование анкеты соискателя"))
        self.ExitButton.setText(_translate("edit_anketa_soiscWindow", "Отменить заполение и выйти"))
        self.label_2.setText(_translate("edit_anketa_soiscWindow", "Прикрепить резюме"))
        self.label.setText(_translate("edit_anketa_soiscWindow", "Редактирование анкеты соискателя"))
        self.label_4.setText(_translate("edit_anketa_soiscWindow", "Опыт работы"))
        self.NoExpButton.setText(_translate("edit_anketa_soiscWindow", "Нет опыта"))
        self.Year_of_expEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Годы"))
        self.Place_expEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Место"))
        self.label_3.setText(_translate("edit_anketa_soiscWindow", "Основная информация"))
        self.lineEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Имя"))
        self.lineEdit_2.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Фамилия"))
        self.lineEdit_3.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Дата рождения"))
        self.lineEdit_4.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Номер телефона"))
        self.lineEdit_5.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Почта"))
        self.lineEdit_6.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Город проживания"))
        self.loadingButton.setText(_translate("edit_anketa_soiscWindow", "Загрузить анкету"))
        self.label_7.setText(_translate("edit_anketa_soiscWindow", "Навыки"))
        self.label_5.setText(_translate("edit_anketa_soiscWindow", "Образование"))
        self.Place_eduEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Место"))
        self.Year_of_educEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Годы"))
        self.SpecialEdit.setPlaceholderText(_translate("edit_anketa_soiscWindow", "Специализация"))
        self.NoEduButton.setText(_translate("load_ankets", "Нет образования"))
        self.NoSkillButton.setText(_translate("load_ankets", "Навыки не указаны"))

class Ui_RecKandidate(object):
    def setupUi(self, RecKandidate, vacancy_id):
        RecKandidate.setObjectName("RecKandidate")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecKandidate.sizePolicy().hasHeightForWidth())
        RecKandidate.setSizePolicy(sizePolicy)
        RecKandidate.showMaximized() 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RecKandidate.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RecKandidate)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(13, 123, 521, 711))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget{font-size: 14pt;}") 
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 80, 521, 31))
        self.frame_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_nameWindow_4 = QtWidgets.QLabel(self.frame_4)
        self.label_nameWindow_4.setGeometry(QtCore.QRect(130, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_4.setFont(font)
        self.label_nameWindow_4.setObjectName("label_nameWindow_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1520, 80, 391, 31))
        self.frame_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_nameWindow_3 = QtWidgets.QLabel(self.frame_3)
        self.label_nameWindow_3.setGeometry(QtCore.QRect(110, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_3.setFont(font)
        self.label_nameWindow_3.setObjectName("label_nameWindow_3")
        self.DescriptionCandidate = QtWidgets.QListWidget(self.centralwidget)
        self.DescriptionCandidate.setGeometry(QtCore.QRect(1520, 160, 391, 671))
        self.DescriptionCandidate.setObjectName("tableCandidate")
        self.DescriptionCandidate.setStyleSheet("QListWidget{font-size: 14pt;}")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(1750, 10, 141, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(750, 0, 591, 51))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_nameWindow = QtWidgets.QLabel(self.frame)
        self.label_nameWindow.setGeometry(QtCore.QRect(70, 0, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_nameWindow.setFont(font)
        self.label_nameWindow.setObjectName("label_nameWindow")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(548, 83, 961, 31))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_nameWindow_2 = QtWidgets.QLabel(self.frame_2)
        self.label_nameWindow_2.setGeometry(QtCore.QRect(500, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nameWindow_2.setFont(font)
        self.label_nameWindow_2.setObjectName("label_nameWindow_2")
        self.tableSois = QtWidgets.QTableView(self.centralwidget)
        self.tableSois.setGeometry(QtCore.QRect(548, 123, 961, 711))
        self.tableSois.setObjectName("tableSois")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 850, 971, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1520, 120, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont("Arial", 10, weight=QtGui.QFont.Bold))
        RecKandidate.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecKandidate)
        QtCore.QMetaObject.connectSlotsByName(RecKandidate)

        ID = vacancy_id  # Get the vacancy ID from the selected row

        cursor = connection.cursor()
        sql_query = "SELECT v.title, v.salary, v.experience, v.adress, v.education, v.skills, v.date_public, emp.name \
                FROM vacancy v \
                INNER JOIN employer emp ON v.employer = emp.id \
                WHERE v.id = %s"   # Query to retrieve all data for the selected vacancy
        cursor.execute(sql_query, (ID,))  # Execute the query with the vacancy ID parameter
        result = cursor.fetchone()  # Retrieve the query result

        if result:  # If information about the vacancy is obtained
            # Clear the appropriate list widget
            self.listWidget.clear()
            self.listWidget.addItem(f"Должность: {result['title']}")
            self.listWidget.addItem(f"Работодатель: {result['name']}")
            self.listWidget.addItem(f"Зарплата: {result['salary']}")
            self.listWidget.addItem(f"Необходимый опыт работы: {result['experience']}")
            self.listWidget.addItem(f"Адрес: {result['adress']}")
            self.listWidget.addItem(f"Образование: {result['education']}")
            self.listWidget.addItem(f"Необходимые навыки: {result['skills']}")
            self.listWidget.addItem(f"Дата публикации: {result['date_public']}")

        else:
            # If information about the vacancy is not found, clear the appropriate list widget
            self.listWidget.clear()

        self.BackButton.clicked.connect(lambda: self.BackToMainWindow(RecKandidate))

        cursor = connection.cursor()

        # SQL-запрос для получения данных о соискателях
        query = "SELECT a.id, CONCAT(a.surname, ' ', a.name) AS full_name, a.status, a.telephone, a.mail FROM Applicant a WHERE a.id NOT IN (SELECT c.id_app FROM candidate c WHERE c.id_vac = %s) ORDER BY FIELD(a.status, 'Новый', 'Просмотрен', 'Подходит на вакансию', 'Принят на работу');"
        cursor.execute(query, (vacancy_id,))
        rows = cursor.fetchall()

        # Создание модели данных для таблицы соискателей
        model = QStandardItemModel(len(rows), 5)  # Количество строк определяется длиной полученных данных, 4 столбца
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус', 'Почта', 'Телефон'])  # Задание заголовков столбцов

        # Заполнение данными из базы данных
        for row_num, row_data in enumerate(rows):
            item_id = QStandardItem(str(row_data['id']))  # ID
            model.setItem(row_num, 0, item_id)

            item_full_name = QStandardItem(row_data['full_name'])  # Фамилия и Имя
            model.setItem(row_num, 1, item_full_name)

            item_status = QStandardItem(row_data['status'])  # Статус
            model.setItem(row_num, 2, item_status)

            item_mail = QStandardItem(row_data['mail'])  # Статус
            model.setItem(row_num, 3, item_mail)

            item_telephone = QStandardItem(row_data['telephone'])  # Телефон
            model.setItem(row_num, 4, item_telephone)
            if row_data['status'] == 'Принят на работу':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['status'] == 'Подходит на вакансию':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['status'] == 'Новый':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))

        self.tableSois.setModel(model)
        self.tableSois.setColumnWidth(0, 20)
        self.tableSois.setColumnWidth(1, 300)  # Ширина первого столбца
        self.tableSois.setColumnWidth(2, 200)  # Ширина второго столбца
        self.tableSois.setColumnWidth(3, 200)  # Ширина третьего столбца
        self.tableSois.setColumnWidth(4, 210)  # Ширина третьего столбца
        self.tableSois.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSois.setSelectionMode(QAbstractItemView.SingleSelection)  # Установить режим выбора одной строки
        self.tableSois.setSelectionBehavior(QAbstractItemView.SelectRows)  # Установить поведение выбора строк
        self.tableSois.clicked.connect(self.showDescription)

        self.pushButton.clicked.connect(lambda: self.addCandidateToTable(vacancy_id, connection, cursor))

    def addCandidateToTable(self, vacancy_id, connection, cursor):
        selected_indexes = self.tableSois.selectedIndexes()
        if not selected_indexes:
            QMessageBox.critical(None, "Ошибка", "Пожалуйста, выберите кандидата!")
            return

        row = selected_indexes[0].row()
        candidate_id = self.tableSois.model().data(self.tableSois.model().index(row, 0))
        with open('account.txt', 'r') as file:
            id_officer = file.read()  

        insert_query = "INSERT INTO Candidate (id_app, id_vac, id_user) VALUES (%s, %s, %s)"
        update_query = "UPDATE Applicant SET status = 'Подходит на вакансию' WHERE id = %s"

        try:
            cursor.execute(insert_query, (candidate_id, vacancy_id, id_officer))
            cursor.execute(update_query, (candidate_id,))
            connection.commit()
            self.fetchDataForTable(vacancy_id)  
            QMessageBox.information(None, "Успешно!", "Кандидат успешно добавлен в таблицу и его статус обновлен.")
        except Exception as e:
            connection.rollback()
            QMessageBox.critical(None, "Ошибка", f"Не удалось добавить кандидата в таблицу. Ошибка: {str(e)}")



    def fetchDataForTable(self, vacancy_id):
        self.listWidget.clear()
        ID = vacancy_id
        cursor = connection.cursor()
        sql_query = "SELECT v.title, v.salary, v.experience, v.adress, v.education, v.skills, v.date_public, emp.name \
                FROM vacancy v \
                INNER JOIN employer emp ON v.employer = emp.id \
                WHERE v.id = %s"   # Запрос для получения всех данных для выбранной вакансии
        cursor.execute(sql_query, (ID,))  # Выполнить запрос с параметром ID вакансии
        result = cursor.fetchone()  # Получить результат запроса

        if result:  # Если получена информация о вакансии
            # Очистить соответствующий список
            self.listWidget.clear()
            self.listWidget.addItem(f"Должность: {result['title']}")
            self.listWidget.addItem(f"Работодатель: {result['name']}")
            self.listWidget.addItem(f"Зарплата: {result['salary']}")
            self.listWidget.addItem(f"Необходимый опыт работы: {result['experience']}")
            self.listWidget.addItem(f"Адрес: {result['adress']}")
            self.listWidget.addItem(f"Образование: {result['education']}")
            self.listWidget.addItem(f"Необходимые навыки: {result['skills']}")
            self.listWidget.addItem(f"Дата публикации: {result['date_public']}")
        else:
            # Если информация о вакансии не найдена, очистить соответствующий список
            self.listWidget.clear()

        cursor = connection.cursor()
        # SQL-запрос для получения данных о соискателях
        query = "SELECT a.id, CONCAT(a.surname, ' ', a.name) AS full_name, a.status, a.telephone, a.mail FROM Applicant a WHERE a.id NOT IN (SELECT c.id_app FROM candidate c WHERE c.id_vac = %s) ORDER BY FIELD(a.status, 'Новый', 'Просмотрен', 'Подходит на вакансию', 'Принят на работу');"
        cursor.execute(query, (vacancy_id,))
        rows = cursor.fetchall()

        # Создать модель данных для таблицы соискателей
        model = QStandardItemModel(len(rows), 5)  # Количество строк определяется длиной полученных данных, 4 столбца
        model.setHorizontalHeaderLabels(['ID', 'ФИ', 'Статус', 'Почта', 'Телефон'])  # Задать заголовки столбцов

        # Заполнение данными из базы данных
        for row_num, row_data in enumerate(rows):
            item_id = QStandardItem(str(row_data['id']))  # ID
            model.setItem(row_num, 0, item_id)

            item_full_name = QStandardItem(row_data['full_name'])  # Фамилия и Имя
            model.setItem(row_num, 1, item_full_name)

            item_status = QStandardItem(row_data['status'])  # Статус
            model.setItem(row_num, 2, item_status)

            item_mail = QStandardItem(row_data['mail'])  # Статус
            model.setItem(row_num, 3, item_mail)

            item_telephone = QStandardItem(row_data['telephone'])  # Телефон
            model.setItem(row_num, 4, item_telephone)
            if row_data['status'] == 'Принят на работу':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(192, 192, 192)))

            elif row_data['status'] == 'Подходит на вакансию':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(157, 210, 255)))

            elif row_data['status'] == 'Новый':
                for col in range(5):
                    model.item(row_num, col).setBackground(QBrush(QColor(217, 255, 198)))

        self.tableSois.setModel(model)
        self.tableSois.setColumnWidth(0, 20)
        self.tableSois.setColumnWidth(1, 300)  # Ширина первого столбца
        self.tableSois.setColumnWidth(2, 200)  # Ширина второго столбца
        self.tableSois.setColumnWidth(3, 200)  # Ширина третьего столбца
        self.tableSois.setColumnWidth(4, 210)  # Ширина третьего столбца
        self.tableSois.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Установить обработчик событий для клика  

    def showDescription(self, index):
        cursor = connection.cursor()
        selected_row = index.row()  # Получаем номер выбранной строки
        applicant_id = self.tableSois.model().index(selected_row, 0).data()  # Получаем id выбранного соискателя

        cursor = connection.cursor()
        sql_query = "SELECT * FROM applicant WHERE id = %s"  # Запрос на получение всех данных выбранной вакансии
        cursor.execute(sql_query, (applicant_id,))  # Выполняем запрос с параметром vacancy_id
        result = cursor.fetchone()  # Получаем результат запроса

        if result:
            self.DescriptionCandidate.clear()
            self.DescriptionCandidate.addItem(f"Имя: {result['name']}")
            self.DescriptionCandidate.addItem(f"Фамилия: {result['surname']}")
            self.DescriptionCandidate.addItem(f"Дата рождения: {result['date_of_birth']}")
            self.DescriptionCandidate.addItem(f"Телефон: {result['telephone']}")
            self.DescriptionCandidate.addItem(f"Почта: {result['mail']}")
            self.DescriptionCandidate.addItem(f"Город проживания: {result['city']}")
            self.DescriptionCandidate.addItem(f"Годы работы: {result['year_ex']}")
            self.DescriptionCandidate.addItem(f"Место работы: {result['place_ex']}")
            self.DescriptionCandidate.addItem(f"Годы образования: {result['year_educ']}")
            self.DescriptionCandidate.addItem(f"Место образования: {result['place_educ']}")
            self.DescriptionCandidate.addItem(f"Специализация: {result['special']}")
            self.DescriptionCandidate.addItem(f"Навыки: {result['skills']}")
            self.lineEdit.setText(f"Статус: {result['status']}")
        else:
            self.DescriptionCandidate.clear()

    def BackToMainWindow(self, RecKandidate):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VacWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        RecKandidate.close()

    def retranslateUi(self, RecKandidate):
        _translate = QtCore.QCoreApplication.translate
        RecKandidate.setWindowTitle(_translate("RecKandidate", "Подходящие кандидаты"))
        self.label_nameWindow_4.setText(_translate("RecKandidate", "Описание выбранной вакансии"))
        self.label_nameWindow_3.setText(_translate("RecKandidate", "Описание соискателя"))
        self.BackButton.setText(_translate("RecKandidate", "Назад"))
        self.label_nameWindow.setText(_translate("RecKandidate", "Подходящие кандидаты"))
        self.label_nameWindow_2.setText(_translate("RecKandidate", "Соискатели"))
        self.pushButton.setText(_translate("RecKandidate", "Соискатель является подходящим кандидатом на вакансию"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
