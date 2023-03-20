from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from ui.src.vlikeengine import Ui_RegWindow
from core.ya_menu import MainW
from core.ya_database import *


class RegW(QMainWindow, Ui_RegWindow):
    def __init__(self):
        # Класс для окна регистрации и меню v-like engine club
        super().__init__()
        self.setupUi(self)
        self.user = ''
        self.loginbut.clicked.connect(self.prepare_enter)
        self.stackedWidget_2.setCurrentIndex(0)
        self.reg_but.clicked.connect(self.go_to_reg)
        self.pass_edit.textChanged.connect(self.pass_check)
        self.name_edit.textChanged.connect(self.reset_error)
        self.surname_edit.textChanged.connect(self.reset_error)
        self.login_edit.textChanged.connect(self.reset_error)
        self.mail.textChanged.connect(self.reset_error)
        self.pass_edit_r.textChanged.connect(self.reset_error)
        self.startyamca.clicked.connect(self.start_yamca)
        self.register_but.clicked.connect(self.try_to_reg)
        self.back_log.clicked.connect(self.back_to_log)
        self.startyamca_2.clicked.connect(self.back_to_log)
        self.pm = QPixmap('./resources/mainmenu_bg.jpg')
        self.bg_label.setPixmap(self.pm)
        self.prem_button.clicked.connect(self.change_premium)
        self.pm1 = QPixmap('./resources/preset.jpg')
        self.presets_show.setPixmap(self.pm1)
        self.pm2 = QPixmap('./resources/presepia.jpg')
        self.presets_show_2.setPixmap(self.pm2)

    def prepare_enter(self):
        self.user = self.loginchoose.currentText()
        if check_user(self.user):
            if self.passwordchoose.text() == get_password(self.user):
                self.enter()
            else:
                self.login_error.setText('Wrong password!')
        else:
            self.login_error.setText('Incorrect login!')

    def enter(self):
        self.stackedWidget_2.setCurrentIndex(2)
        self.name_surname.setText(get_names(self.user) + '!')
        self.login_edit.setText('')
        self.pass_edit.setText('')
        self.pass_edit_r.setText('')
        self.name_edit.setText('')
        self.surname_edit.setText('')
        self.mail.setText('')
        self.premium_button_pref()
        self.pm = QPixmap('./resources/newsmenu_bg.jpg')
        self.bg_label.setPixmap(self.pm)

    def premium_button_pref(self):
        if get_prem(self.user):
            self.prem_button.setText('Leave Premium program')
            self.prem_label.setText('You are premium! Thank you for subscription. We really appreciate your help!')
        else:
            self.prem_button.setText('Get Premium!')
            self.prem_label.setText('Get more options for only 2$ per month!')

    def start_yamca(self):
        self.m_w = MainW(self, self.user, get_prem(self.user), get_theme(self.user))
        self.m_w.setWindowModality(Qt.ApplicationModal)
        self.m_w.show()

    def go_to_reg(self):
        self.login_error.setText('')
        self.stackedWidget_2.setCurrentIndex(1)

    def back_to_log(self):
        self.error.setText('')
        self.stackedWidget_2.setCurrentIndex(0)
        self.pm = QPixmap('./resources/mainmenu_bg.jpg')
        self.bg_label.setPixmap(self.pm)

    def try_to_reg(self):
        if len(self.login_edit.text()) == 0 or self.login_edit.text().isdigit():
            self.error.setText('Incorrect login!')
        elif self.pass_edit.text() != self.pass_edit_r.text():
            self.error.setText('Passwords do not match')
        elif self.hardness_pass.text() != 'Hard':
            self.error.setText('Password is too easy! Use upper- and lowcase words and use numbers')
        elif len(self.name_edit.text()) == 0 or not (self.name_edit.text().isalpha()):
            self.error.setText('You need a correct, non-number name')
        elif len(self.surname_edit.text()) == 0 or not (self.surname_edit.text().isalpha()):
            self.error.setText('You need a correct, non-number surname')
        elif len(self.mail.text()) == 0 or '@' not in self.mail.text():
            self.error.setText('Use a correct mail adress!')
        elif not (self.agree_with.isChecked()):
            self.error.setText('You need to agree with ALL!')
        else:
            t = '1' if self.get_prem.isChecked() else '0'
            new_user(self.login_edit.text(), self.pass_edit.text(), self.name_edit.text(),
                     self.surname_edit.text(), self.mail.text(), self.year_box.text(), t)
            self.user = self.login_edit.text()
            self.enter()

    def reset_error(self):
        self.error.setText('')

    def change_premium(self):
        if get_prem(self.user):
            premium_forget(self.user)
            self.premium_button_pref()
        else:
            premium_access(self.user)
            self.premium_button_pref()

    def pass_check(self):
        self.error.setText('')
        if len(self.pass_edit.text()) <= 6:
            self.progressBar.setValue(len(self.pass_edit.text()) * 2)
            self.hardness_pass.setText('Too easy')
        else:
            val = len(self.pass_edit.text()) * 3 if len(self.pass_edit.text()) < 25 else \
                abs(100 - len(self.pass_edit.text()))
            if self.pass_edit.text().isdigit():
                self.progressBar.setValue(val)
                self.hardness_pass.setText('No letters')
            elif self.pass_edit.text().isalpha():
                self.progressBar.setValue(val)
                self.hardness_pass.setText('No numbers')
            elif self.pass_edit.text() == self.pass_edit.text().lower():
                self.progressBar.setValue(val)
                self.hardness_pass.setText('No uppercase')
            elif self.pass_edit.text() == self.pass_edit.text().upper():
                self.progressBar.setValue(val)
                self.hardness_pass.setText('No lowercase')
            else:
                self.progressBar.setValue(100)
                self.hardness_pass.setText('Hard')
