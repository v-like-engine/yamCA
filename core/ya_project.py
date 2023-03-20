import shutil

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QColorDialog, QMessageBox, QInputDialog

from core.ya_database import preset_values, get_presets_name, append_preset, title_exists, delete_preset
from core.ya_pil import YaMage
from core.ya_design_change import change_design, projectw_solid_bg, projectw_label_fg
from core.image_to_qt import save_qt_version, get_sizes
from ui.src.projectwindow import Ui_ProjectWindow
from PyQt5.QtGui import QPixmap, QIcon


class ProjW(QMainWindow, Ui_ProjectWindow):
    def __init__(self, parent, filename, user, design, premium, issavingmmry):
        # Класс основного окна работы с изображениями
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.filename = filename
        self.user = user
        if not(premium):
            self.actionSave_preset.setDisabled(True)
            self.actionDelete_all_custom_presets.setDisabled(True)
            self.create_preset.setDisabled(True)
            self.delete_preset.setDisabled(True)
            self.label_3.setText('Get a premium to be able to save & use custom presets!')
        self.issavingmmry = issavingmmry
        self.palettefunc = self.one_palette
        self.x, self.y, self.x1, self.y1 = 0, 0, 0, 0
        self.coltochange = 0
        self.image_worker.setCurrentIndex(5)
        self.setWindowTitle("YAMCA: {}".format(filename))
        self.image = YaMage(filename, user)
        sizes = self.image.size
        self.sizes = get_sizes(sizes)
        self.qtim_filename = save_qt_version(self.image.path, filename, self.sizes, False)
        self.pm = QPixmap(self.qtim_filename)
        self.space_2.setMinimumSize((1136 - self.sizes[0]) // 2, 600)
        self.label_for_image.setPixmap(self.pm)
        self.imageplacement = [122 + (900 - self.image.y) // 2, 1 + (600 - self.image.x) // 2]

        if premium:
            presets = get_presets_name(self.user)
            self.numpreset = 5
            for i in range(len(presets)):
                self.comboBox.insertItem(self.numpreset, presets[i][0])
                self.numpreset += 1
            self.label_3.setText('included ' + str(self.numpreset - 5) + ' user presets')

        self.actionDelete.triggered.connect(self.back_to_menu)
        self.actionSave_as.triggered.connect(self.save_image)
        self.deslabels = [self.color_label_1, self.color_label_2, self.color_label_3, self.color_label_4,
                          self.color_label_5, self.color_label_6, self.color_label_7, self.color_label_8]
        self.desbuttons = [self.luminance_button, self.mixing_button, self.palette_button,
                           self.shadow_color_button, self.light_color_button, self.presets_button,
                           self.resize_button, self.spin_left_button, self.spin_right_button,
                           self.delete_preset, self.create_preset, self.accept_luminance,
                           self.open_color_dialog, self.apply_preset, self.append_mix, self.cancel_mix,
                           self.x_set, self.y_set, self.size_set]
        self.lightlabels = [self.label_3, self.mxing_color, self.mxing_color_2, self.mxing_color_3,
                            self.lumilabel, self.lumilabel_2, self.label_luminance, self.label_contrast,
                            self.color_mixing_func_label, self.relabel, self.yelabel, self.grlabel, self.cylabel,
                            self.blabel, self.pulabel, self.shade_cm_label, self.sat_cm_label, self.bright_cm_label,
                            self.cursize_label, self.label, self.label_2]
        self.change_design_func(design)
        self.actionYandex.triggered.connect(self.yandex_design)
        self.actionDarkened_foremost.triggered.connect(self.darkened_design)
        self.actionDark_Theme.triggered.connect(self.theme_design)
        self.actionDark_Leaps.triggered.connect(self.leaps_design)
        self.actionGradient.triggered.connect(self.gradi_design)
        self.actionOrange_gradient.triggered.connect(self.orgradi_design)
        self.actionGradark.triggered.connect(self.gradark_design)
        self.accept_luminance.clicked.connect(self.luminance)
        self.colormix_buttons.buttonClicked.connect(self.colormix_prepare)
        self.create_preset.clicked.connect(self.new_preset)
        self.check_ability_to_delete_preset()
        self.comboBox.currentIndexChanged.connect(self.check_ability_to_delete_preset)
        self.delete_preset.clicked.connect(self.del_preset)

        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionReset_all_changes.triggered.connect(self.reset_all)
        self.actionSave_preset.triggered.connect(self.new_preset)

        self.luminance_button.clicked.connect(self.menu_luminance)
        self.mixing_button.clicked.connect(self.menu_mixing)
        self.palette_button.clicked.connect(self.palfc)
        self.shadow_color_button.clicked.connect(self.shfg)
        self.light_color_button.clicked.connect(self.lgfg)
        self.resize_button.clicked.connect(self.menu_resize)
        self.spin_left_button.clicked.connect(self.rotate_left)
        self.spin_right_button.clicked.connect(self.rotate_right)
        self.presets_button.clicked.connect(self.menu_presets)

        self.x_set.clicked.connect(self.setx)
        self.y_set.clicked.connect(self.sety)
        self.size_set.clicked.connect(self.set_resize)
        self.append_mix.clicked.connect(self.start_mx)
        self.cancel_mix.clicked.connect(self.menu_mixing)
        self.open_color_dialog.clicked.connect(self.expalette)
        self.apply_preset.clicked.connect(self.append_filter)

        self.luminance_button.setIcon(QIcon('./resources/icons/luminance.png'))
        self.luminance_button.setIconSize(QSize(60, 60))
        self.mixing_button.setIcon(QIcon('./resources/icons/palette.png'))
        self.mixing_button.setIconSize(QSize(60, 60))
        self.shadow_color_button.setIcon(QIcon('./resources/icons/_yang.png'))
        self.shadow_color_button.setIconSize(QSize(60, 60))
        self.light_color_button.setIcon(QIcon('./resources/icons/in_yang.png'))
        self.light_color_button.setIconSize(QSize(60, 60))
        self.spin_right_button.setIcon(QIcon('./resources/icons/rot_right.png'))
        self.spin_right_button.setIconSize(QSize(60, 60))
        self.spin_left_button.setIcon(QIcon('./resources/icons/rot_left.png'))
        self.spin_left_button.setIconSize(QSize(60, 60))
        self.presets_button.setIcon(QIcon('./resources/icons/setups.png'))
        self.presets_button.setIconSize(QSize(60, 60))
        self.resize_button.setIcon(QIcon('./resources/icons/resize.png'))
        self.resize_button.setIconSize(QSize(60, 60))
        self.palette_button.setIcon(QIcon('./resources/icons/brush.png'))
        self.palette_button.setIconSize(QSize(60, 60))
        self.actionRedo.setDisabled(True)

    def getqcolor(self):
        return QColorDialog.getColor().getRgb()

    def print_color(self):
        print(self.getqcolor())

    def lightfight(self):
        self.image.new_savename(self.issavingmmry)
        self.image.colorfight(self.getqcolor(), True)
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def shadowfight(self):
        self.image.new_savename(self.issavingmmry)
        self.image.colorfight(self.getqcolor(), False)
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def one_palette(self):
        self.image.new_savename(self.issavingmmry)
        self.image.palette_onecol(self.getqcolor())
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def yandex_design(self):
        change_design(self.deslabels, 0)
        projectw_solid_bg(self.desbuttons, 0)
        projectw_label_fg(self.lightlabels, 0)

    def darkened_design(self):
        change_design(self.deslabels, 1)
        projectw_solid_bg(self.desbuttons, 1)
        projectw_label_fg(self.lightlabels, 1)

    def theme_design(self):
        change_design(self.deslabels, 2)
        projectw_solid_bg(self.desbuttons, 2)
        projectw_label_fg(self.lightlabels, 2)

    def leaps_design(self):
        change_design(self.deslabels, 3)
        projectw_solid_bg(self.desbuttons, 3)
        projectw_label_fg(self.lightlabels, 3)

    def gradi_design(self):
        change_design(self.deslabels, 4)
        projectw_solid_bg(self.desbuttons, 4)
        projectw_label_fg(self.lightlabels, 4)

    def orgradi_design(self):
        change_design(self.deslabels, 5)
        projectw_solid_bg(self.desbuttons, 5)
        projectw_label_fg(self.lightlabels, 5)

    def gradark_design(self):
        change_design(self.deslabels, 6)
        projectw_solid_bg(self.desbuttons, 6)
        projectw_label_fg(self.lightlabels, 6)

    def back_to_menu(self):
        shutil.rmtree(self.image.path)
        self.close()
        self.parent.show()

    def change_design_func(self, index):
        change_design(self.deslabels, index)
        if index in [0, 1, 2]:
            projectw_solid_bg(self.desbuttons, index)

    def colormix_prepare(self, btn):
        self.image_worker.setCurrentIndex(3)
        if btn == self.red_button:
            self.mxing_color.setText('Red color settings')
            self.csh.setValue(self.image.red[0])
            self.csat.setValue(self.image.red[1])
            self.cbr.setValue(self.image.red[2])
            self.coltochange = 1
        elif btn == self.yellow_button_2:
            self.mxing_color.setText('Yellow color settings')
            self.csh.setValue(self.image.yellow[0])
            self.csat.setValue(self.image.yellow[1])
            self.cbr.setValue(self.image.yellow[2])
            self.coltochange = 2
        elif btn == self.green_button:
            self.mxing_color.setText('Green color settings')
            self.csh.setValue(self.image.green[0])
            self.csat.setValue(self.image.green[1])
            self.cbr.setValue(self.image.green[2])
            self.coltochange = 3
        elif btn == self.cyan_button:
            self.mxing_color.setText('Cyan color settings')
            self.csh.setValue(self.image.cyan[0])
            self.csat.setValue(self.image.cyan[1])
            self.cbr.setValue(self.image.cyan[2])
            self.coltochange = 4
        elif btn == self.blue_button:
            self.mxing_color.setText('Blue color settings')
            self.csh.setValue(self.image.blue[0])
            self.csat.setValue(self.image.blue[1])
            self.cbr.setValue(self.image.blue[2])
            self.coltochange = 5
        elif btn == self.purple_button:
            self.mxing_color.setText('Purple color settings')
            self.csh.setValue(self.image.purple[0])
            self.csat.setValue(self.image.purple[1])
            self.cbr.setValue(self.image.purple[2])
            self.coltochange = 6

    def start_mx(self):
        self.mx_color(self.coltochange)

    def mx_color(self, color):
        self.image.new_savename(self.issavingmmry)
        self.image.mx_color(color, self.csh.value(), self.csat.value(), self.cbr.value())
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def lgfg(self):
        self.palettefunc = self.lightfight
        self.menu_palette()
        self.lumilabel_2.setText('Light Palette Change')

    def shfg(self):
        self.palettefunc = self.shadowfight
        self.menu_palette()
        self.lumilabel_2.setText('Shadow Palette Change')

    def palfc(self):
        self.palettefunc = self.one_palette
        self.menu_palette()
        self.lumilabel_2.setText('Palette Change')

    def menu_luminance(self):
        self.image_worker.setCurrentIndex(0)

    def menu_mixing(self):
        self.image_worker.setCurrentIndex(2)

    def menu_palette(self):
        self.image_worker.setCurrentIndex(1)

    def menu_resize(self):
        self.image_worker.setCurrentIndex(4)
        self.cursize_label.setText(self.cursize_label.text().split(':')[0] + ': {} x {}'.format(self.image.y,
                                                                                                self.image.x))
        self.x_resize.setValue(self.image.y)
        self.y_resize.setValue(self.image.x)

    def menu_presets(self):
        self.image_worker.setCurrentIndex(5)

    def expalette(self):
        self.palettefunc()

    def setx(self):
        self.y_resize.setValue(int(self.image.x / self.image.y * self.x_resize.value()))

    def sety(self):
        self.x_resize.setValue(int(self.image.y / self.image.x * self.y_resize.value()))

    def set_resize(self):
        self.image.new_savename(self.issavingmmry)
        self.image.newy = self.x_resize.value()
        self.image.newx = self.y_resize.value()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()
        self.cursize_label.setText(self.cursize_label.text().split(':')[0] + ': {} x {}'.format(self.image.y,
                                                                                                self.image.x))
        self.imageplacement = [122 + (900 - self.image.y) // 2, 1 + (600 - self.image.x) // 2]

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.ControlModifier):
            if event.key() == Qt.Key_Z or event.key() == ord('Я'):
                self.undo()
        elif int(event.modifiers()) == (Qt.ControlModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_Z or event.key() == ord('Я'):
                self.redo()
        elif event.key() == Qt.Key_C or event.key() == ord('С'):
            self.menu_palette()
        elif event.key() == Qt.Key_S or event.key() == ord('Ы'):
            self.menu_palette()
        elif event.key() == Qt.Key_B or event.key() == ord('И'):
            self.menu_luminance()
        elif event.key() == Qt.Key_K or event.key() == ord('Л'):
            self.menu_mixing()
        elif event.key() == Qt.Key_P or event.key() == ord('З'):
            self.menu_palette()
        elif event.key() == Qt.Key_I or event.key() == ord('Ш'):
            self.menu_resize()
        elif event.key() == Qt.Key_R or event.key() == ord('К'):
            self.rotate_right()
        elif event.key() == Qt.Key_L or event.key() == ord('Д'):
            self.rotate_left()
        elif event.key() == Qt.Key_M or event.key() == ord('Ь'):
            self.menu_presets()

    def getsave(self):
        return QFileDialog.getSaveFileName(self, 'save', '', 'Image (*.jpg)')

    def black_white(self):
        self.image.new_savename(self.issavingmmry)
        self.image.black_and_white_one()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def conturs(self):
        self.image.new_savename(self.issavingmmry)
        self.image.contur()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def pure_colors(self):
        self.image.new_savename(self.issavingmmry)
        self.image.pure_colours()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def negative(self):
        self.image.new_savename(self.issavingmmry)
        self.image.negative()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def sepia(self):
        self.image.new_savename(self.issavingmmry)
        self.image.sepia()
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def luminance(self):
        if self.image.luminance(self.lumislider.value()):
            self.image.new_savename(self.issavingmmry)
            self.image.make_it_an_image(self.image.savename, True)
            self.to_qt()
        if self.image.contrast(self.conslider.value()):
            self.image.new_savename(self.issavingmmry)
            self.image.make_it_an_image(self.image.savename, True)
            self.to_qt()

    def rotate_left(self):
        self.image.new_savename(self.issavingmmry)
        self.image.miai_with_rotate(self.image.savename, 0)
        self.sizes = get_sizes((self.image.y, self.image.x))
        self.space_2.setMinimumSize((1136 - self.sizes[0]) // 2, 600)
        self.to_qt()

    def rotate_right(self):
        self.image.new_savename(self.issavingmmry)
        self.image.miai_with_rotate(self.image.savename, 1)
        self.sizes = get_sizes((self.image.y, self.image.x))
        self.space_2.setMinimumSize((1136 - self.sizes[0]) // 2, 600)
        self.to_qt()

    def check_ability_to_delete_preset(self):
        if self.comboBox.currentIndex() == 0:
            self.delete_preset.setDisabled(True)
        elif self.comboBox.currentIndex() == 1:
            self.delete_preset.setDisabled(True)
        elif self.comboBox.currentIndex() == 2:
            self.delete_preset.setDisabled(True)
        elif self.comboBox.currentIndex() == 3:
            self.delete_preset.setDisabled(True)
        elif self.comboBox.currentIndex() == 4:
            self.delete_preset.setDisabled(True)
        else:
            self.delete_preset.setEnabled(True)

    def append_filter(self):
        if self.comboBox.currentIndex() == 0:
            self.black_white()
        elif self.comboBox.currentIndex() == 1:
            self.negative()
        elif self.comboBox.currentIndex() == 2:
            self.sepia()
        elif self.comboBox.currentIndex() == 3:
            self.conturs()
        elif self.comboBox.currentIndex() == 4:
            self.pure_colors()
        else:
            values = preset_values(self.comboBox.currentText())
            self.use_preset(values)

    def use_preset(self, values):
        logstr = ''
        donestr = ''
        if self.image.luminance(values[3]):
            logstr += 'self.image.' + self.image.log.pop(-1) + '; '
            donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        if self.image.contrast(values[4]):
            logstr += 'self.image.' + self.image.log.pop(-1) + '; '
            donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(1, values[5], values[6], values[7])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(2, values[8], values[9], values[10])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(3, values[11], values[12], values[13])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(4, values[14], values[15], values[16])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(5, values[17], values[18], values[19])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.mx_color(6, values[20], values[21], values[22])
        logstr += 'self.image.' + self.image.log.pop(-1) + '; '
        donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        if values[23] != '""' and values[23] != '':
            val = list(map(int, values[23][1:-1].split(', ')))
            self.image.palette_onecol(val)
            logstr += 'self.image.' + self.image.log.pop(-1) + '; '
            donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        if values[24] != '""' and values[24] != '':
            val = list(map(int, values[24][1:-1].split(', ')))
            self.image.colorfight(val, True)
            logstr += 'self.image.' + self.image.log.pop(-1) + '; '
            donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        if values[25] != '""' and values[25] != '':
            val = list(map(int, values[25][1:-1].split(', ')))
            self.image.colorfight(val, False)
            logstr += 'self.image.' + self.image.log.pop(-1) + '; '
            donestr += 'self.image.' + self.image.done.pop(-1) + '; '
        self.image.log.append(logstr[12:-1])
        self.image.done.append(donestr[12:-1])
        self.image.new_savename(self.issavingmmry)
        self.image.make_it_an_image(self.image.savename, True)
        self.to_qt()

    def check_title(self, title):
        if title_exists(self.user, title) or title in ('Black & White', 'Negative', 'Sepia',
                                                       'Sketch', 'Pure colors', ''):
            return self.check_title(title[:-1] + str(int(title[-1]) + 1))
        return title

    def new_preset(self):
        title, done = QInputDialog.getText(self, "Set the name of preset", "What is the title of preset?")
        if done:
            if title_exists(self.user, title) or title in ('Black & White', 'Negative', 'Sepia',
                                                           'Sketch', 'Pure colors', ''):
                title = self.check_title(title + '_1')
            values = [self.image.lum, self.image.cont, self.image.red, self.image.yellow, self.image.green,
                      self.image.cyan, self.image.blue, self.image.purple, self.image.palette,
                      self.image.light, self.image.shadow]
            append_preset(self.user, title, values)
            self.comboBox.insertItem(self.numpreset, title)
            self.numpreset += 1
            self.label_3.setText('included ' + str(self.numpreset - 5) + ' user presets')

    def del_preset(self):
        title = self.comboBox.currentText()
        if not title in ('Black & White', 'Negative', 'Sepia', 'Sketch', 'Pure colors', ''):
            try:
                delete_preset(self.user, title)
                self.comboBox.removeItem(self.comboBox.currentIndex())
            except Exception:
                print('can not delete preset ' + title + ' from user' + self.user + '`s preset library: database error')

    def save_image(self):
        svname = '.'.join(self.getsave()[0].split('.')[:-1])
        if svname:
            self.image.make_it_an_image(svname, False)

    def undo(self):
        if self.image.numcopy > 0 and self.image.mincopy < self.image.numcopy:
            self.image.numcopy -= 1
            t = self.image.log.pop(-1)
            self.image.unlog.append(t)
            if t:
                exec('self.image.' + t)
            self.image.undone.append(self.image.done.pop(-1))
            nsvname = self.image.get_last_save()
            self.image.fromimage(self.image.path + '/' + nsvname)
            self.qtim_filename = save_qt_version(self.image.path, nsvname, get_sizes(self.image.size), True)
            self.pm = QPixmap(self.qtim_filename)
            self.label_for_image.setPixmap(self.pm)
            self.actionRedo.setEnabled(True)

    def redo(self):
        if self.image.maxcopy > self.image.numcopy and self.actionRedo.isEnabled():
            self.image.numcopy += 1
            t = self.image.undone.pop(-1)
            self.image.done.append(t)
            if t:
                exec('self.image.' + t)
            self.image.log.append(self.image.unlog.pop(-1))
            nsvname = self.image.get_last_save()
            self.image.fromimage(self.image.path + '/' + nsvname)
            self.qtim_filename = save_qt_version(self.image.path, nsvname, get_sizes(self.image.size), True)
            self.pm = QPixmap(self.qtim_filename)
            self.label_for_image.setPixmap(self.pm)
            if self.image.maxcopy == self.image.numcopy:
                self.actionRedo.setDisabled(True)

    def reset_all(self):
        self.buttonReply = QMessageBox.question(self, 'You`re going to reset all changes. That`s a bold move!',
                                                "All of your changes made on this photo will be lost. Continue?",
                                                QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if self.buttonReply == QMessageBox.Ok:
            self.image_worker.setCurrentIndex(5)
            self.image = YaMage(self.filename, self.user)
            sizes = self.image.size
            self.sizes = get_sizes(sizes)
            self.qtim_filename = save_qt_version(self.image.path, self.filename, self.sizes, False)
            self.pm = QPixmap(self.qtim_filename)
            self.space_2.setMinimumSize((1136 - self.sizes[0]) // 2, 600)
            self.label_for_image.setPixmap(self.pm)
            self.imageplacement = [122 + (900 - self.image.y) // 2, 1 + (600 - self.image.x) // 2]

    def to_qt(self):
        self.qtim_filename = save_qt_version(self.image.path, self.image.savename + self.image.filetype,
                                             self.sizes, True)
        self.pm = QPixmap(self.qtim_filename)
        self.label_for_image.setPixmap(self.pm)
        self.actionRedo.setDisabled(True)

    def closeEvent(self, event):
        self.parent.show()
