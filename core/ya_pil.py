from PIL import Image
import numpy as np
import os


class YaMage:
    def __init__(self, filename, username):
        # Класс для работы с изображениями, все фильтры и опции, в т.ч. применение пресетов (может занять много времени)
        self.filetype = '.' + filename.split('.')[-1]
        getname = filename.split('/')[-1]
        self.name = '.'.join(getname.split('.')[:-1])
        self.numcopy = 0
        self.maxcopy = 0
        self.mincopy = 0
        self.savename = username + '_' + self.name + '_' + str(self.numcopy)
        self.user = username
        self.fromimage(filename)
        self.size = self.im.size
        self.unlog = []
        self.log = ['']
        self.undone = []
        self.done = []
        self.lum = 0
        self.cont = 0
        self.red = [0, 0, 0]
        self.yellow = [0, 0, 0]
        self.green = [0, 0, 0]
        self.cyan = [0, 0, 0]
        self.blue = [0, 0, 0]
        self.purple = [0, 0, 0]
        self.palette = '""'
        self.light = '""'
        self.shadow = '""'
        self.newx = self.x
        self.newy = self.y
        self.path = './temp/' + self.name
        try:
            os.mkdir(self.path)
        except OSError:
            print('can`t make directory', self.path + ': directory already exists')
        self.make_it_an_image(self.savename, True)

    def black_and_white_one(self):
        self.done.append('')
        self.log.append('')
        self.maxcopy = self.numcopy
        self.npimage[0] = self.npimage[0] * 0.2989
        self.npimage[1] = self.npimage[1] * 0.5870
        self.npimage[2] = self.npimage[2] * 0.1140
        self.prepare_for_miai()
        self.npimage = np.repeat(np.round(np.sum(self.npimage, axis=-1)), 3)
        self.prepare_after_miai()

    def pure_colours(self):
        self.done.append('')
        self.log.append('')
        self.maxcopy = self.numcopy
        self.npimage[0] = np.array([0 if v < 128 else 255 for v in self.npimage[0]])
        self.npimage[1] = np.array([0 if v < 128 else 255 for v in self.npimage[1]])
        self.npimage[2] = np.array([0 if v < 128 else 255 for v in self.npimage[2]])

    def contur(self):
        self.done.append('')
        self.log.append('')
        self.maxcopy = self.numcopy
        self.pure_colours()
        self.prepare_for_miai()
        self.npimage = np.repeat(np.round(np.sum(self.npimage, axis=-1)), 3)
        self.prepare_after_miai()

    def negative(self):
        self.done.append('')
        self.log.append('')
        self.maxcopy = self.numcopy
        self.npimage[0] = np.array([255 - v for v in self.npimage[0]])
        self.npimage[1] = np.array([255 - v for v in self.npimage[1]])
        self.npimage[2] = np.array([255 - v for v in self.npimage[2]])

    def sepia(self):
        self.done.append('')
        self.log.append('')
        self.maxcopy = self.numcopy
        self.prepare_for_miai()
        x, y = self.x, self.y
        for i in range(x):
            for j in range(y):
                r, g, b = self.npimage[i, j]
                new_col = (min(255, max(0, int(r * 0.393 + g * 0.769 + b * 0.189))),
                           min(255, max(0, int(r * 0.349 + g * 0.686 + b * 0.168))),
                           min(255, max(0, int(r * 0.272 + g * 0.534 + b * 0.131))))
                self.npimage[i, j] = new_col
        self.prepare_after_miai()

    def luminance(self, value):
        if value != self.lum:
            self.log.append('lum = ' + str(self.lum))
            self.npimage[0] = np.array([min(255, max(0, v + value - self.lum)) for v in self.npimage[0]])
            self.npimage[1] = np.array([min(255, max(0, v + value - self.lum)) for v in self.npimage[1]])
            self.npimage[2] = np.array([min(255, max(0, v + value - self.lum)) for v in self.npimage[2]])
            self.lum = value
            self.done.append('lum = ' + str(self.lum))
            self.maxcopy = self.numcopy
            return True
        return False

    def contrast(self, value):
        if value != self.cont:
            self.log.append('cont = ' + str(self.cont))
            factor = (259 * (value - self.cont + 255)) / (255 * (259 - value + self.cont))
            self.npimage[0] = np.array([min(255, max(0, 128 + factor * (v - 128))) for v in self.npimage[0]])
            self.npimage[1] = np.array([min(255, max(0, 128 + factor * (v - 128))) for v in self.npimage[1]])
            self.npimage[2] = np.array([min(255, max(0, 128 + factor * (v - 128))) for v in self.npimage[2]])
            self.cont = value
            self.done.append('cont = ' + str(self.cont))
            self.maxcopy = self.numcopy
            return True
        return False

    def colorfight(self, color, light_fight):
        self.prepare_for_miai()
        col = [0, 0, 0]
        col[0] = color[0] / 255
        col[1] = color[1] / 255
        col[2] = color[2] / 255
        x, y = self.x, self.y
        self.maxcopy = self.numcopy
        if light_fight:
            self.log.append('light = ' + str(self.light))
            self.done.append('light = ' + str(color))
            self.light = str(color)
        else:
            self.log.append('shadow = ' + str(self.shadow))
            self.done.append('shadow = ' + str(color))
            self.shadow = str(color)
        for i in range(x):
            for j in range(y):
                r, g, b = self.npimage[i, j]
                avcol = (r + g + b) // 3
                if light_fight:
                    avcolcof = avcol / 255
                else:
                    avcolcof = 1 - avcol / 255
                new_col = (min(255, int(avcolcof * col[0] * 255 + r)),
                           min(255, int(avcolcof * col[1] * 255 + g)),
                           min(255, int(avcolcof * col[2] * 255 + b)))
                self.npimage[i, j] = new_col
        self.prepare_after_miai()

    def palette_onecol(self, color):
        self.prepare_for_miai()
        col = [0, 0, 0]
        col[0] = color[0] / 255
        col[1] = color[1] / 255
        col[2] = color[2] / 255
        x, y = self.x, self.y
        self.maxcopy = self.numcopy
        self.log.append('palette = ' + str(self.palette))
        self.palette = str(color)
        self.done.append('palette = ' + str(self.palette))
        for i in range(x):
            for j in range(y):
                r, g, b = self.npimage[i, j]
                avcol = (r + g + b) // 3
                new_col = (min(255, int(avcol * col[0])),
                           min(255, int(avcol * col[1])),
                           min(255, int(avcol * col[2])))
                self.npimage[i, j] = new_col
        self.prepare_after_miai()

    def mx_color(self, color, shade, sat, br):
        self.prepare_for_miai()
        if color == 1:
            self.log.append('red = ' + str(self.red))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        self.npimage[i, j] = self.pure_color_help(self.red, r, g, b, shade, sat, br)
            self.red = [shade, sat, br]
            self.done.append('red = ' + str(self.red))
        elif color == 2:
            self.log.append('yellow = ' + str(self.yellow))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        t = self.dual_color_help(self.yellow, r, g, b, shade, sat, br)
                        self.npimage[i, j] = t
            self.yellow = [shade, sat, br]
            self.done.append('yellow = ' + str(self.yellow))
        elif color == 3:
            self.log.append('green = ' + str(self.green))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        t = self.pure_color_help(self.red, g, r, b, shade, sat, br)
                        self.npimage[i, j] = t[1], t[0], t[2]
            self.green = [shade, sat, br]
            self.done.append('green = ' + str(self.green))
        elif color == 4:
            self.log.append('cyan = ' + str(self.cyan))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        t = self.dual_color_help(self.cyan, g, b, r, shade, sat, br)
                        self.npimage[i, j] = t[2], t[0], t[1]
            self.cyan = [shade, sat, br]
            self.done.append('cyan = ' + str(self.cyan))
        elif color == 5:
            self.log.append('blue = ' + str(self.blue))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        t = self.pure_color_help(self.red, b, r, g, shade, sat, br)
                        self.npimage[i, j] = t[1], t[2], t[0]
            self.blue = [shade, sat, br]
            self.done.append('blue = ' + str(self.blue))
        elif color == 6:
            self.log.append('purple = ' + str(self.purple))
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.npimage[i, j]
                    if r + g + b != 0:
                        t = self.dual_color_help(self.purple, r, b, g, shade, sat, br)
                        self.npimage[i, j] = t[0], t[2], t[1]
            self.purple = [shade, sat, br]
            self.done.append('purple = ' + str(self.purple))
        self.prepare_after_miai()

    def pure_color_help(self, cc, r, g, b, shade, sat, br):
        if (r + g + b) != 0:
            if int(r) / int(r + g + b) > 0.5:
                if cc[0] != shade:
                    if cc[0] >= 0 and shade >= 0:
                        b = max(0, min(255, b - cc[0] + shade))
                    elif cc[0] > 0 and shade <= 0:
                        g = min(255, g - shade)
                        b = max(0, b - cc[0])
                    elif cc[0] < 0 and shade >= 0:
                        b = min(255, b + shade)
                        g = max(0, g + cc[0])
                    elif cc[0] <= 0 and shade <= 0:
                        g = max(0, min(255, g + cc[0] - shade))
                if cc[1] != sat:
                    r = min(255, max(0, r + sat - cc[1]))
                if cc[2] != br:
                    r = min(255, max(0, r + br - cc[2]))
                    g = min(255, max(0, g + br - cc[2]))
                    b = min(255, max(0, b + br - cc[2]))
        return [r, g, b]

    def dual_color_help(self, cc, r, g, b, shade, sat, br):
        if (r + g + b) != 0:
            if int(r + g) / int(r + g + b) > 0.8 and int(r + g) / int(r + g + b) / 2 - 0.1 < int(r) / int(r + g + b) < \
                    int(r + g) / int(r + g + b) / 2 + 0.1:
                if cc[0] != shade:
                    if cc[0] >= 0 and shade >= 0:
                        g = max(0, min(255, g - cc[0] + shade))
                        r = max(0, min(255, r + cc[0] - shade))
                    elif cc[0] > 0 and shade <= 0:
                        r = min(255, g - shade + cc[0])
                        g = max(0, g - cc[0] + shade)
                    elif cc[0] < 0 and shade >= 0:
                        g = min(255, b + shade - cc[0])
                        r = max(0, g + cc[0] - shade)
                    elif cc[0] <= 0 and shade <= 0:
                        r = max(0, min(255, r + cc[0] - shade))
                        g = max(0, min(255, g - cc[0] + shade))
                if cc[1] != sat:
                    r = min(255, max(0, r + sat - cc[1]))
                    g = min(255, max(0, g + sat - cc[1]))
                if cc[2] != br:
                    r = min(255, max(0, r + br - cc[2]))
                    g = min(255, max(0, g + br - cc[2]))
                    b = min(255, max(0, b + br - cc[2]))
        return [r, g, b]

    def new_savename(self, issavingmmry):
        self.numcopy += 1
        self.maxcopy += 1
        self.savename = '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy)
        if self.numcopy > 2:
            try:
                os.remove(self.path + '/' + '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy - 2)
                          + '_qtv' + self.filetype)
            except OSError:
                print(self.path + '/' + '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy - 2)
                      + '_qtv' + self.filetype)
        if self.numcopy > 10 and issavingmmry:
            try:
                os.remove(self.path + '/' + '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy - 10)
                          + self.filetype)
                self.mincopy += 1
            except OSError:
                print(self.path + '/' + '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy - 10)
                      + self.filetype)

    def prepare_for_miai(self):
        self.npimage = self.npimage.transpose()
        self.npimage = self.npimage.reshape(self.x, self.y, 3)

    def make_it_an_image(self, name, temp):
        self.prepare_for_miai()
        image = Image.fromarray(np.uint8(self.npimage))
        if self.newx != self.x or self.newy != self.y:
            self.log.append('')
            image = image.resize((self.newy, self.newx))
            self.done.append('')
        if temp:
            image.save(self.path + '/' + name + self.filetype)
        else:
            image.save(name + self.filetype)
        self.prepare_after_miai()

    def prepare_after_miai(self):
        self.npimage = self.npimage.reshape(self.x * self.y, 3)
        self.npimage = self.npimage.transpose()

    def miai_with_rotate(self, name, dir):
        self.prepare_for_miai()
        if dir == 0:
            im = Image.fromarray(np.uint8(self.npimage))
            im = im.transpose(Image.ROTATE_90)
            im.save(self.path + '/' + name + self.filetype)
            self.npimage = np.array(im, dtype='float64')
            self.im = im
        else:
            im = Image.fromarray(np.uint8(self.npimage))
            im = im.transpose(Image.ROTATE_270)
            im.save(self.path + '/' + name + self.filetype)
            self.npimage = np.array(im, dtype='float64')
            self.im = im
        self.maxcopy = self.numcopy
        self.log.append('x, self.image.y, self.image.size = {}, {}, {}'.format(self.x, self.y, self.size))
        self.x, self.y = self.y, self.x
        self.size = self.im.size
        self.done.append('x, self.image.y, self.image.size = {}, {}, {}'.format(self.x, self.y, self.size))
        self.prepare_after_miai()

    def fromimage(self, filename):
        self.im = Image.open(filename)
        self.npimage = np.array(self.im, dtype='float64')
        self.stockx, self.stocky = len(self.npimage), len(self.npimage[0])
        self.x, self.y = len(self.npimage), len(self.npimage[0])
        self.prepare_after_miai()

    def get_last_save(self):
        return '_'.join(self.savename.split('_')[:-1]) + '_' + str(self.numcopy) + self.filetype
