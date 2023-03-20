import random

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from core.ya_database import update_design
from core.ya_project import ProjW
from core.ya_design_change import change_design
from ui.src.ui_mainW import Ui_MainWindow


class MainW(QMainWindow, Ui_MainWindow):
    def __init__(self, parent, user, prem, theme):
        # Класс для окна меню
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.parent = parent
        self.prem = prem
        self.stackedWidget.setCurrentIndex(0)
        self.preferences.clicked.connect(self.pref_show)
        self.back_from_pref.clicked.connect(self.pref_hide)
        self.newprojbut.clicked.connect(self.work_at_project_menu)
        self.back_from_pref_2.clicked.connect(self.pref_hide)
        self.designcombo.currentIndexChanged.connect(self.change_design_func)
        self.deslabels = [self.color_label_1, self.color_label_2, self.color_label_3, self.color_label_4,
                          self.color_label_5, self.color_label_6, self.color_label_7, self.color_label_8]
        self.exitbut.clicked.connect(self.exit)
        self.startproject.clicked.connect(self.choose_image_file)
        self.myfont()
        self.changeaccb.clicked.connect(self.change_acc)
        self.change_design_func(theme)
        self.random_design.clicked.connect(self.random_theme)
        self.designcombo.setCurrentIndex(theme)
        self.image = None

    def myfont(self):
        try:
            idbs = QFontDatabase.addApplicationFont("./resources/BadScript-Regular.ttf")
            badscriptfamily = QFontDatabase.applicationFontFamilies(idbs)[0]
            self.setStyleSheet('* { font-family: "' + badscriptfamily + '" }')
        except Exception:
            print('Can not use custom font: Bad Script =(')

    def pref_show(self):
        self.stackedWidget.setCurrentIndex(1)

    def pref_hide(self):
        self.stackedWidget.setCurrentIndex(0)

    def work_at_project_menu(self):
        self.stackedWidget.setCurrentIndex(2)

    def change_acc(self):
        self.parent.stackedWidget_2.setCurrentIndex(0)
        self.hide()

    def start_new_project(self, filename):
        self.hide()
        if self.tutorialcheck.isChecked():
            self.pr_w = ProjW(self, filename, self.user, self.theme, self.prem, True)
        else:
            self.pr_w = ProjW(self, filename, self.user, self.theme, self.prem, False)
        self.pr_w.show()

    def choose_image_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Image', '',
                                                'Image' + '(*.jpg *.bmp)')[0]
        if file_name:
            self.start_new_project(file_name)

    def random_theme(self):
        index = random.randint(0, 6)
        self.change_design_func(index)

    def change_design_func(self, index):
        change_design(self.deslabels, index)
        if index in [2, 3, 6]:
            self.mcalabel_3.setStyleSheet('color: "#8c8c8c"')
            self.mcalabel_4.setStyleSheet('color: "#8c8c8c"')
            self.mcalabel_5.setStyleSheet('color: "#8c8c8c"')
            self.authority.setStyleSheet('color: "#8c8c8c"')
            self.tutorialcheck.setStyleSheet('color: "#8c8c8c"')
        else:
            self.mcalabel_3.setStyleSheet('color: "#000"')
            self.mcalabel_4.setStyleSheet('color: "#000"')
            self.mcalabel_5.setStyleSheet('color: "#000"')
            self.authority.setStyleSheet('color: "#000"')
            self.tutorialcheck.setStyleSheet('color: "#000"')
        self.theme = index

    def exit(self):
        update_design(self.user, str(self.theme))
        self.close()
