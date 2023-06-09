# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlikeengine.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        RegWindow.setObjectName("RegWindow")
        RegWindow.resize(1080, 800)
        self.centralwidget = QtWidgets.QWidget(RegWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_label = QtWidgets.QLabel(self.centralwidget)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 1080, 800))
        self.bg_label.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(11, 82, 156, 255), stop:0.659091 rgba(108, 162, 255, 212), stop:0.9375 rgba(89, 169, 210, 216));")
        self.bg_label.setText("")
        self.bg_label.setObjectName("bg_label")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 1080, 800))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.loginwin = QtWidgets.QWidget()
        self.loginwin.setObjectName("loginwin")
        self.logindialog = QtWidgets.QLabel(self.loginwin)
        self.logindialog.setGeometry(QtCore.QRect(240, 30, 600, 680))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.logindialog.setFont(font)
        self.logindialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logindialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(50, 84, 160, 255), stop:0.488636 rgba(137, 169, 209, 234), stop:1 rgba(155, 232, 255, 212));")
        self.logindialog.setTextFormat(QtCore.Qt.AutoText)
        self.logindialog.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.logindialog.setObjectName("logindialog")
        self.loginchoose = QtWidgets.QComboBox(self.loginwin)
        self.loginchoose.setGeometry(QtCore.QRect(300, 220, 480, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.loginchoose.setFont(font)
        self.loginchoose.setEditable(True)
        self.loginchoose.setObjectName("loginchoose")
        self.loginchoose.addItem("")
        self.passwordchoose = QtWidgets.QLineEdit(self.loginwin)
        self.passwordchoose.setGeometry(QtCore.QRect(300, 300, 480, 40))
        self.passwordchoose.setText("")
        self.passwordchoose.setMaxLength(40)
        self.passwordchoose.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordchoose.setObjectName("passwordchoose")
        self.loginbut = QtWidgets.QPushButton(self.loginwin)
        self.loginbut.setGeometry(QtCore.QRect(300, 380, 480, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.loginbut.setFont(font)
        self.loginbut.setObjectName("loginbut")
        self.no_acc = QtWidgets.QLabel(self.loginwin)
        self.no_acc.setGeometry(QtCore.QRect(300, 488, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.no_acc.setFont(font)
        self.no_acc.setObjectName("no_acc")
        self.reg_but = QtWidgets.QPushButton(self.loginwin)
        self.reg_but.setGeometry(QtCore.QRect(490, 480, 290, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.reg_but.setFont(font)
        self.reg_but.setObjectName("reg_but")
        self.login_error = QtWidgets.QLabel(self.loginwin)
        self.login_error.setGeometry(QtCore.QRect(300, 550, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.login_error.setFont(font)
        self.login_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.login_error.setText("")
        self.login_error.setObjectName("login_error")
        self.stackedWidget_2.addWidget(self.loginwin)
        self.regwin = QtWidgets.QWidget()
        self.regwin.setObjectName("regwin")
        self.progressBar = QtWidgets.QProgressBar(self.regwin)
        self.progressBar.setGeometry(QtCore.QRect(680, 170, 130, 30))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.register_main_label = QtWidgets.QLabel(self.regwin)
        self.register_main_label.setGeometry(QtCore.QRect(240, 30, 600, 680))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.register_main_label.setFont(font)
        self.register_main_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_main_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(50, 84, 160, 255), stop:0.488636 rgba(137, 169, 209, 234), stop:1 rgba(155, 232, 255, 212));")
        self.register_main_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.register_main_label.setObjectName("register_main_label")
        self.login_edit = QtWidgets.QLineEdit(self.regwin)
        self.login_edit.setGeometry(QtCore.QRect(390, 120, 420, 30))
        self.login_edit.setObjectName("login_edit")
        self.label_3 = QtWidgets.QLabel(self.regwin)
        self.label_3.setGeometry(QtCore.QRect(250, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.regwin)
        self.label_4.setGeometry(QtCore.QRect(250, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.pass_edit = QtWidgets.QLineEdit(self.regwin)
        self.pass_edit.setGeometry(QtCore.QRect(390, 170, 271, 30))
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        self.pass_edit_r = QtWidgets.QLineEdit(self.regwin)
        self.pass_edit_r.setGeometry(QtCore.QRect(390, 220, 271, 30))
        self.pass_edit_r.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit_r.setObjectName("pass_edit_r")
        self.label_5 = QtWidgets.QLabel(self.regwin)
        self.label_5.setGeometry(QtCore.QRect(250, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.regwin)
        self.label_6.setGeometry(QtCore.QRect(250, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.regwin)
        self.label_7.setGeometry(QtCore.QRect(250, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.year_box = QtWidgets.QSpinBox(self.regwin)
        self.year_box.setGeometry(QtCore.QRect(390, 370, 111, 30))
        self.year_box.setMinimum(1919)
        self.year_box.setMaximum(2018)
        self.year_box.setProperty("value", 1996)
        self.year_box.setObjectName("year_box")
        self.name_edit = QtWidgets.QLineEdit(self.regwin)
        self.name_edit.setGeometry(QtCore.QRect(390, 270, 420, 30))
        self.name_edit.setObjectName("name_edit")
        self.surname_edit = QtWidgets.QLineEdit(self.regwin)
        self.surname_edit.setGeometry(QtCore.QRect(390, 320, 420, 30))
        self.surname_edit.setObjectName("surname_edit")
        self.hardness_pass = QtWidgets.QLabel(self.regwin)
        self.hardness_pass.setGeometry(QtCore.QRect(680, 220, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.hardness_pass.setFont(font)
        self.hardness_pass.setObjectName("hardness_pass")
        self.label_8 = QtWidgets.QLabel(self.regwin)
        self.label_8.setGeometry(QtCore.QRect(250, 420, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.mail = QtWidgets.QLineEdit(self.regwin)
        self.mail.setGeometry(QtCore.QRect(390, 420, 420, 30))
        self.mail.setObjectName("mail")
        self.get_prem = QtWidgets.QCheckBox(self.regwin)
        self.get_prem.setGeometry(QtCore.QRect(270, 470, 541, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.get_prem.setFont(font)
        self.get_prem.setObjectName("get_prem")
        self.agree_with = QtWidgets.QCheckBox(self.regwin)
        self.agree_with.setGeometry(QtCore.QRect(270, 510, 541, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.agree_with.setFont(font)
        self.agree_with.setObjectName("agree_with")
        self.register_but = QtWidgets.QPushButton(self.regwin)
        self.register_but.setGeometry(QtCore.QRect(260, 580, 560, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setItalic(True)
        self.register_but.setFont(font)
        self.register_but.setObjectName("register_but")
        self.label_9 = QtWidgets.QLabel(self.regwin)
        self.label_9.setGeometry(QtCore.QRect(250, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.error = QtWidgets.QLabel(self.regwin)
        self.error.setGeometry(QtCore.QRect(266, 539, 550, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.error.setFont(font)
        self.error.setStyleSheet("color: rgb(255, 0, 0);")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.back_log = QtWidgets.QPushButton(self.regwin)
        self.back_log.setGeometry(QtCore.QRect(260, 650, 560, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.back_log.setFont(font)
        self.back_log.setObjectName("back_log")
        self.register_main_label.raise_()
        self.progressBar.raise_()
        self.login_edit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pass_edit.raise_()
        self.pass_edit_r.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.year_box.raise_()
        self.name_edit.raise_()
        self.surname_edit.raise_()
        self.hardness_pass.raise_()
        self.label_8.raise_()
        self.mail.raise_()
        self.get_prem.raise_()
        self.agree_with.raise_()
        self.register_but.raise_()
        self.label_9.raise_()
        self.error.raise_()
        self.back_log.raise_()
        self.stackedWidget_2.addWidget(self.regwin)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.welcome = QtWidgets.QLabel(self.page)
        self.welcome.setGeometry(QtCore.QRect(10, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.label_space = QtWidgets.QLabel(self.page)
        self.label_space.setGeometry(QtCore.QRect(500, 10, 5, 781))
        self.label_space.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space.setText("")
        self.label_space.setObjectName("label_space")
        self.name_surname = QtWidgets.QLabel(self.page)
        self.name_surname.setGeometry(QtCore.QRect(10, 70, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        self.name_surname.setFont(font)
        self.name_surname.setText("")
        self.name_surname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_surname.setObjectName("name_surname")
        self.startyamca = QtWidgets.QPushButton(self.page)
        self.startyamca.setGeometry(QtCore.QRect(10, 270, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(False)
        self.startyamca.setFont(font)
        self.startyamca.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.startyamca.setObjectName("startyamca")
        self.news_heading = QtWidgets.QLabel(self.page)
        self.news_heading.setGeometry(QtCore.QRect(520, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        self.news_heading.setFont(font)
        self.news_heading.setObjectName("news_heading")
        self.news_heading_2 = QtWidgets.QLabel(self.page)
        self.news_heading_2.setGeometry(QtCore.QRect(520, 70, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.news_heading_2.setFont(font)
        self.news_heading_2.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.news_heading_2.setObjectName("news_heading_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 360, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_space_2 = QtWidgets.QLabel(self.page)
        self.label_space_2.setGeometry(QtCore.QRect(502, 60, 531, 5))
        self.label_space_2.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_2.setText("")
        self.label_space_2.setObjectName("label_space_2")
        self.label_space_3 = QtWidgets.QLabel(self.page)
        self.label_space_3.setGeometry(QtCore.QRect(520, 120, 300, 2))
        self.label_space_3.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_3.setText("")
        self.label_space_3.setObjectName("label_space_3")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(520, 140, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.presets_show = QtWidgets.QLabel(self.page)
        self.presets_show.setGeometry(QtCore.QRect(560, 280, 200, 200))
        self.presets_show.setText("")
        self.presets_show.setObjectName("presets_show")
        self.presets_show_2 = QtWidgets.QLabel(self.page)
        self.presets_show_2.setGeometry(QtCore.QRect(800, 280, 200, 200))
        self.presets_show_2.setText("")
        self.presets_show_2.setObjectName("presets_show_2")
        self.startyamca_2 = QtWidgets.QPushButton(self.page)
        self.startyamca_2.setGeometry(QtCore.QRect(10, 450, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(False)
        self.startyamca_2.setFont(font)
        self.startyamca_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.startyamca_2.setObjectName("startyamca_2")
        self.news_heading_3 = QtWidgets.QLabel(self.page)
        self.news_heading_3.setGeometry(QtCore.QRect(520, 490, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.news_heading_3.setFont(font)
        self.news_heading_3.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.news_heading_3.setObjectName("news_heading_3")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(520, 560, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_space_4 = QtWidgets.QLabel(self.page)
        self.label_space_4.setGeometry(QtCore.QRect(520, 540, 300, 2))
        self.label_space_4.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_4.setText("")
        self.label_space_4.setObjectName("label_space_4")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(520, 240, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.news_heading_4 = QtWidgets.QLabel(self.page)
        self.news_heading_4.setGeometry(QtCore.QRect(520, 170, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.news_heading_4.setFont(font)
        self.news_heading_4.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.news_heading_4.setObjectName("news_heading_4")
        self.label_space_5 = QtWidgets.QLabel(self.page)
        self.label_space_5.setGeometry(QtCore.QRect(520, 220, 300, 2))
        self.label_space_5.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_5.setText("")
        self.label_space_5.setObjectName("label_space_5")
        self.prem_button = QtWidgets.QPushButton(self.page)
        self.prem_button.setGeometry(QtCore.QRect(520, 720, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setItalic(True)
        self.prem_button.setFont(font)
        self.prem_button.setObjectName("prem_button")
        self.prem_label = QtWidgets.QLabel(self.page)
        self.prem_label.setGeometry(QtCore.QRect(520, 680, 541, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.prem_label.setFont(font)
        self.prem_label.setObjectName("prem_label")
        self.news_heading_5 = QtWidgets.QLabel(self.page)
        self.news_heading_5.setGeometry(QtCore.QRect(520, 610, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.news_heading_5.setFont(font)
        self.news_heading_5.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.news_heading_5.setObjectName("news_heading_5")
        self.label_space_6 = QtWidgets.QLabel(self.page)
        self.label_space_6.setGeometry(QtCore.QRect(520, 660, 300, 2))
        self.label_space_6.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_6.setText("")
        self.label_space_6.setObjectName("label_space_6")
        self.label_space_7 = QtWidgets.QLabel(self.page)
        self.label_space_7.setGeometry(QtCore.QRect(500, 600, 531, 5))
        self.label_space_7.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label_space_7.setText("")
        self.label_space_7.setObjectName("label_space_7")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(770, 371, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.stackedWidget_2.addWidget(self.page)
        RegWindow.setCentralWidget(self.centralwidget)
        self.actionEnglish = QtWidgets.QAction(RegWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.action = QtWidgets.QAction(RegWindow)
        self.action.setObjectName("action")
        self.actionDeutch = QtWidgets.QAction(RegWindow)
        self.actionDeutch.setObjectName("actionDeutch")

        self.retranslateUi(RegWindow)
        self.stackedWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "V-Like Engine Menu"))
        self.logindialog.setText(_translate("RegWindow", "\n"
"Log into V-LikeEngine account"))
        self.loginchoose.setCurrentText(_translate("RegWindow", "Yandex"))
        self.loginchoose.setItemText(0, _translate("RegWindow", "Yandex"))
        self.loginbut.setText(_translate("RegWindow", "Log in"))
        self.no_acc.setText(_translate("RegWindow", "• Do not have an account yet?"))
        self.reg_but.setText(_translate("RegWindow", "Register!"))
        self.progressBar.setFormat(_translate("RegWindow", "%p%"))
        self.register_main_label.setText(_translate("RegWindow", "\n"
"Register V-LikeEngine account"))
        self.label_3.setText(_translate("RegWindow", "Password:"))
        self.label_4.setText(_translate("RegWindow", "Password repeat:"))
        self.label_5.setText(_translate("RegWindow", "Name:"))
        self.label_6.setText(_translate("RegWindow", "Surname:"))
        self.label_7.setText(_translate("RegWindow", "Birth year:"))
        self.hardness_pass.setText(_translate("RegWindow", "Enter Password"))
        self.label_8.setText(_translate("RegWindow", "E-Mail:"))
        self.get_prem.setText(_translate("RegWindow", "Get Premium (free access for 1 month, then 125 P (2$) per month)"))
        self.agree_with.setText(_translate("RegWindow", "I am agree with ALL (alternative licence list)"))
        self.register_but.setText(_translate("RegWindow", "Register"))
        self.label_9.setText(_translate("RegWindow", "Login:"))
        self.back_log.setText(_translate("RegWindow", "Back to Log-in"))
        self.welcome.setText(_translate("RegWindow", "Welcome,"))
        self.startyamca.setText(_translate("RegWindow", "Start YaMCA"))
        self.news_heading.setText(_translate("RegWindow", "V-Like Engine Club News:"))
        self.news_heading_2.setText(_translate("RegWindow", "YaMCA Change Notes v0.1.8"))
        self.pushButton_2.setText(_translate("RegWindow", "Coming soon..."))
        self.label.setText(_translate("RegWindow", "• Custom Presets support! (Premium only function)"))
        self.startyamca_2.setText(_translate("RegWindow", "Leave Account"))
        self.news_heading_3.setText(_translate("RegWindow", "YaMCA Change Notes v0.1.6"))
        self.label_2.setText(_translate("RegWindow", "• Undo & Redo! Closer look on a hotkeys and much more!"))
        self.label_10.setText(_translate("RegWindow", "Introduced presets!"))
        self.news_heading_4.setText(_translate("RegWindow", "YaMCA Change Notes v0.1.7"))
        self.prem_button.setText(_translate("RegWindow", "Get Premium!"))
        self.prem_label.setText(_translate("RegWindow", "Get more options for only 2$ per month!"))
        self.news_heading_5.setText(_translate("RegWindow", "YaMCA Premium access"))
        self.label_11.setText(_translate("RegWindow", ">>"))
        self.actionEnglish.setText(_translate("RegWindow", "English"))
        self.action.setText(_translate("RegWindow", "Русский"))
        self.actionDeutch.setText(_translate("RegWindow", "Deutsch"))
