from main import types,cursor,bd
from parser_tengri import *

def start_inline():
    inl_klav = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("❔Узнай", callback_data="btn1")
    btn2 = types.InlineKeyboardButton("💚Жизнь", callback_data="btn2")
    btn3 = types.InlineKeyboardButton("⚽Спорт", callback_data="btn3")
    btn4 = types.InlineKeyboardButton("✈Вокруг мира", callback_data="btn4")
    btn5 = types.InlineKeyboardButton("📖Почитай", callback_data="btn5")
    btn6 = types.InlineKeyboardButton("👀Посмотри", callback_data="btn6")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return inl_klav

def choice():
    inl_klav = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Все категории", callback_data="all_kat")
    btn2 = types.InlineKeyboardButton("Выбрать подкатегорию", callback_data="choice_kat")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="nazad")
    inl_klav.add(btn1, btn2, btn3)
    return inl_klav

def novosti_yznai_pochitai_posmotri(link, stup, user_id):
    if stup == 1:
        otvet = Tengri_Posmotri_pochitai_yznai(link)
        text = otvet[0]
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (otvet[1][0], otvet[1][1], otvet[1][2], otvet[1][3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        otvet = Tengri_Posmotri_pochitai_yznai(link)
        text = otvet[0]
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (otvet[1][4], otvet[1][5], otvet[1][6], otvet[1][7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        otvet = Tengri_Posmotri_pochitai_yznai(link)
        text = otvet[0]
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (otvet[1][8], otvet[1][9], otvet[1][10], otvet[1][11], user_id,))
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_vpered")
        btn6 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav

def keyboard_travel():
    inl_klav = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("Моя Страна", callback_data="pod1")
    btn2 = types.InlineKeyboardButton("Вокруг Света", callback_data="pod2")
    btn3 = types.InlineKeyboardButton("Путевые Заметки", callback_data="pod3")
    btn4 = types.InlineKeyboardButton("Маршруты Заилийского Алатау", callback_data="pod4")
    btn5 = types.InlineKeyboardButton("Саяхат Time", callback_data="pod5")
    btn6 = types.InlineKeyboardButton("Реклама", callback_data="reklama3")
    btn7 = types.InlineKeyboardButton("Назад", callback_data="nazad")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return inl_klav

def all_keyboard_travel(stup,user_id):
    otvet = All_travel()
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[4], link[5], link[6], link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_vpered")
        btn6 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav

def keyboard_travel_pod1(link_news,stup,user_id):
    otvet = Tengri_Travel(link_news)
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[4], link[5], link[6], link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton("", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav


def keyboard_life():
    inl_klav = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("Красиво", callback_data="pod1")
    btn2 = types.InlineKeyboardButton("Выгодно", callback_data="pod2")
    btn3 = types.InlineKeyboardButton("Полезно", callback_data="pod3")
    btn4 = types.InlineKeyboardButton("Любопытно", callback_data="pod4")
    btn5 = types.InlineKeyboardButton("Гороскопы", callback_data="pod5")
    btn6 = types.InlineKeyboardButton("Реклама", callback_data="reklama")
    btn7 = types.InlineKeyboardButton("Назад", callback_data="nazad")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return inl_klav

def all_keyboard_life(stup,user_id):
    otvet = All_life()
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[4], link[5], link[6], link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_vpered")
        btn6 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav

def keyboard_life_pod1(link_news,stup,user_id):
    otvet = Tengri_Life(link_news)
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[4], link[5], link[6], link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton("", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav


def keyboard_sport():
    inl_klav = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("Спорт", callback_data="pod1")
    btn2 = types.InlineKeyboardButton("Вокруг Спорта", callback_data="pod2")
    btn3 = types.InlineKeyboardButton("Тренды", callback_data="pod3")
    btn4 = types.InlineKeyboardButton("Лига Чемпионов", callback_data="pod4")
    btn5 = types.InlineKeyboardButton("Лига Европы", callback_data="pod5")
    btn6 = types.InlineKeyboardButton("Реклама", callback_data="reklama2")
    btn7 = types.InlineKeyboardButton("Назад", callback_data="nazad")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return inl_klav

def all_keyboard_sport(stup, user_id):
    otvet = All_sport()
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute("UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
                       (link[4],link[5],link[6],link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_vpered")
        btn6 = types.InlineKeyboardButton("<", callback_data="all_nazad")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav

def keyboard_sport_pod1(link_news,stup,user_id):
    otvet = Tengri_Sport(link_news)
    text = otvet[0]
    link = otvet[1]
    if stup == 1:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[0], link[1], link[2], link[3], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 2:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[4], link[5], link[6], link[7], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[4]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[5]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[6]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[7]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton(">", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav
    elif stup == 3:
        cursor.execute(
            "UPDATE `parser_novosti_pod` SET `nov_link1` =?, `nov_link2`=?, `nov_link3`=?, `nov_link4` =? WHERE `user_id` =? ",
            (link[8], link[9], link[10], link[11], user_id,))
        bd.commit()
        inl_klav = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(f"{text[8]}", callback_data="nov_pod1")
        btn2 = types.InlineKeyboardButton(f"{text[9]}", callback_data="nov_pod2")
        btn3 = types.InlineKeyboardButton(f"{text[10]}", callback_data="nov_pod3")
        btn4 = types.InlineKeyboardButton(f"{text[11]}", callback_data="nov_pod4")
        btn5 = types.InlineKeyboardButton("<", callback_data="all_nazad_pod")
        btn6 = types.InlineKeyboardButton("", callback_data="all_vpered_pod")
        btn7 = types.InlineKeyboardButton("В выбор категорий", callback_data="nazad_pod")
        inl_klav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return inl_klav

def keyboard_sport_pod4(link):
    otvet = Tengri_Sport_league(link)
    text = otvet[0]
    inl_klav = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov_pod1")
    btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov_pod2")
    btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov_pod3")
    btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov_pod4")
    btn5 = types.InlineKeyboardButton("Назад", callback_data="nazad_pod")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5)
    return inl_klav

def keyboard_sport_pod5(link):
    otvet = Tengri_Sport_league(link)
    text = otvet[0]
    inl_klav = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f"{text[0]}", callback_data="nov_pod1")
    btn2 = types.InlineKeyboardButton(f"{text[1]}", callback_data="nov_pod2")
    btn3 = types.InlineKeyboardButton(f"{text[2]}", callback_data="nov_pod3")
    btn4 = types.InlineKeyboardButton(f"{text[3]}", callback_data="nov_pod4")
    btn5 = types.InlineKeyboardButton("Назад", callback_data="nazad_pod")
    inl_klav.add(btn1, btn2, btn3, btn4, btn5)
    return inl_klav