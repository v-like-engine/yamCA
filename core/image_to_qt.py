from PIL import Image
# вспомогательные функции преобразования изображения в qt


def save_qt_version(path, filename, sizes, exists):
    filetype = '.' + filename.split('.')[-1]
    getname = filename.split('/')[-1]
    name = '.'.join(getname.split('.')[:-1])
    savename = path + '/' + name + '_qtv' + filetype
    if not exists:
        qt_im = Image.open(filename).resize(sizes)
    else:
        qt_im = Image.open(path + '/' + filename).resize(sizes)
    qt_im.save(savename)
    return savename


def get_sizes(sizes):
    if sizes[0] > 900:
        sizes = (900, int(sizes[1] * 900 / sizes[0]))
    if sizes[1] > 600:
        sizes = (int(sizes[0] * 600 / sizes[1]), 600)
    return sizes
