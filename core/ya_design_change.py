def change_design(deslabels, index):
    if index == 0:
        fast_design_function(deslabels, '#fc0')
    elif index == 1:
        fast_design_function(deslabels, '#cb9b00')
    elif index == 2:
        fast_design_function(deslabels, '#181818')
    elif index == 3:
        fast_design_function(deslabels, '#181818', '#282828', '#383838')
    elif index == 4:
        tempst = []
        for i in range(len(deslabels)):
            tempst.append('rgb(255, {}, 0)'.format(str((len(deslabels) + i) * 17)))
        fast_design_function(deslabels, *tempst)
    elif index == 5:
        tempst = []
        for i in range(len(deslabels)):
            tempst.append('rgb(255, {}, 0)'.format(str(40 + (len(deslabels) + i) * 10)))
        fast_design_function(deslabels, *tempst)
    elif index == 6:
        tempst = []
        for i in range(len(deslabels)):
            tempst.append('rgb({})'.format(', '.join([str((i + 1) * 10 if i < len(deslabels) // 2 else
                                                          (len(deslabels) - i) * 10) for j in range(3)])))
        fast_design_function(deslabels, *tempst)


def fast_design_function(deslabels, *args):
    if len(deslabels) % len(args) == 0:
        for i in range(len(deslabels)):
            deslabels[i].setStyleSheet("background-color: " + args[i // (len(deslabels) // len(args))] + ';')
    else:
        for i in range(len(deslabels)):
            j = i
            k = i // len(args)
            if k >= 1:
                j -= k * len(args)
            deslabels[i].setStyleSheet("background-color: " + args[j] + ';')


def projectw_solid_bg(desbuttons, index):
    if index == 0:
        for i in range(len(desbuttons)):
            desbuttons[i].setStyleSheet("background-color: #fc0")
    elif index == 1:
        for i in range(len(desbuttons)):
            desbuttons[i].setStyleSheet("background-color: #cb9b00")
    elif index in (2, 3, 6):
        for i in range(len(desbuttons)):
            desbuttons[i].setStyleSheet("background-color: #484848")
    else:
        for i in range(len(desbuttons)):
            desbuttons[i].setStyleSheet("")


def projectw_label_fg(lightlabels, index):
    if index in (0, 1, 4, 5):
        for i in range(len(lightlabels)):
            lightlabels[i].setStyleSheet("color: #000")
    elif index in (2, 3, 6):
        for i in range(len(lightlabels)):
            lightlabels[i].setStyleSheet("color: #8c8c8c")