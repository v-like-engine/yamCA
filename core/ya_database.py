import sqlite3
# Работа с базой данных, добавление пользователей и пресетов


def append_preset(user, title, preset_values, base='./resources/users.db'):
    title = title
    lum = preset_values[0]
    cont = preset_values[1]
    red_sh = preset_values[2][0]
    red_sat = preset_values[2][1]
    red_br = preset_values[2][2]
    yellow_sh = preset_values[3][0]
    yellow_sat = preset_values[3][1]
    yellow_br = preset_values[3][2]
    green_sh = preset_values[4][0]
    green_sat = preset_values[4][1]
    green_br = preset_values[4][2]
    cyan_sh = preset_values[5][0]
    cyan_sat = preset_values[5][1]
    cyan_br = preset_values[5][2]
    blue_sh = preset_values[6][0]
    blue_sat = preset_values[6][1]
    blue_br = preset_values[6][2]
    purple_sh = preset_values[7][0]
    purple_sat = preset_values[7][1]
    purple_br = preset_values[7][2]
    palette = str(preset_values[8])
    light = str(preset_values[9])
    shadow = str(preset_values[10])
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('insert into filters(user_id, title, luminance, contrast, red_shade, red_sat, red_br, ' +
                'yellow_shade, yellow_sat, yellow_br, green_shade, green_sat, green_br, cyan_shade, cyan_sat, ' +
                'cyan_br, blue_shade, blue_sat, blue_br, purple_shade, purple_sat, purple_br, palette, ' +
                'light_color, shadow_color) values((select id from users where username = ?), ?, ?, ?, ?, ?, ?, ?, ?,' +
                '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user, title, lum, cont, red_sh, red_sat, red_br,
                                                                    yellow_sh, yellow_sat, yellow_br, green_sh,
                                                                    green_sat, green_br, cyan_sh, cyan_sat, cyan_br,
                                                                    blue_sh, blue_sat, blue_br, purple_sh, purple_sat,
                                                                    purple_br, palette, light, shadow, ))
    conn.commit()


def title_exists(user, title, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select title from filters where user_id = (select id from users where username = "' +
                      user + '") and title = "' + title + '"').fetchall()
    if res:
        return True
    else:
        return False


def preset_values(title, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select * from filters where title = "' + title + '"').fetchall()
    return res[0]


def delete_preset(user, title, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('delete from filters where user_id = (select id from users where username = "' + user +
                '") and title = "' + title + '"')
    conn.commit()


def get_presets_name(user, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    res = cur.execute('select title from filters where user_id = (select id from users where username = "' +
                      user + '")').fetchall()
    return res


def new_user(username, password, name, surname, email, birthyear, prem, base='./resources/users.db'):
    username = '"' + username + '"'
    password = '"' + password + '"'
    name = '"' + name + '"'
    surname = '"' + surname + '"'
    email = '"' + email + '"'
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    do_this = 'insert into users (username, password, name, surname, email, birthyear, design, premium_access)' +\
              ' values (' + ', '.join([username, password, name, surname, email, birthyear, '0', prem]) + ')'
    cur.execute(do_this)
    conn.commit()


def check_user(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    res = cur.execute('select * from users where username = "' + username + '"').fetchall()
    if res:
        return True
    else:
        return False


def get_password(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    res = cur.execute('select * from users where username = "' + username + '"').fetchall()
    conn.close()
    return res[0][2]


def get_names(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    res = cur.execute('select * from users where username = "' + username + '"').fetchall()
    conn.close()
    return res[0][4] + ' ' + res[0][3]


def get_prem(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    res = cur.execute('select * from users where username = "' + username + '"').fetchall()
    conn.close()
    return True if res[0][8] == 1 else False


def get_theme(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    res = cur.execute('select * from users where username = "' + username + '"').fetchall()
    conn.close()
    return res[0][7]


def update_design(username, theme, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('update users set design = ' + theme + ' where username = "' + username + '"')
    conn.commit()


def premium_access(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('update users set premium_access = 1 where username = "' + username + '"')
    conn.commit()


def premium_forget(username, base='./resources/users.db'):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('update users set premium_access = 0 where username = "' + username + '"')
    conn.commit()
