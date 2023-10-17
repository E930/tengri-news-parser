import sqlite3
from inline_keyboard import *
from parser_tengri_news import *
bd = sqlite3.connect("tengri.db")
cursor = bd.cursor()

def bd_tengri (user_id,blog):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?",(user_id,)).fetchall()
    if len(user) == 0:
        cursor.execute("INSERT OR IGNORE INTO `blogi_pod` (`user_id`, `user_blog_pod`, `stup`) VALUES (?,?,?)",(user_id, blog,0,))
        bd.commit()
        cursor.execute("INSERT OR IGNORE INTO `blogi` (`user_id`, `user_blog`, `stup`) VALUES (?,?,?)",(user_id, blog,0,))
        bd.commit()
        cursor.execute("INSERT OR IGNORE INTO `parser_novosti` (`nov_link1`,`nov_link2`,`nov_link3`,`nov_link4`, `user_id`) VALUES (?,?,?,?,?)",(1,2,3,4, user_id,))
        bd.commit()
        cursor.execute("INSERT OR IGNORE INTO `parser_novosti_pod` (`nov_link1`,`nov_link2`,`nov_link3`,`nov_link4`, `user_id`) VALUES (?,?,?,?,?)",(1,2,3,4, user_id,))
        bd.commit()
    else:
        cursor.execute("UPDATE `blogi` SET `user_blog` =? WHERE `user_id` =?",(blog,user_id))
        bd.commit()
    return f"Ваш блог обновлён на <b>{blog}</b>"


def podkat(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    if user[0][0] == "Спорт":
        otvet = keyboard_sport()
        return otvet
    elif user[0][0] == "Вокруг мира":
        otvet = keyboard_travel()
        return otvet
    elif user[0][0] == "Жизнь":
        otvet = keyboard_life()
        return otvet

def podkat1(user_id,pod):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi_pod` WHERE `user_id` =?", (user_id,)).fetchall()
    if user_stup[0][0] == 0:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =?, `user_blog_pod` =? WHERE `user_id` =?", (1, pod, user_id,))
        bd.commit()
    elif user_stup[0][0] == 1:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =?, `user_blog_pod` =? WHERE `user_id` =?", (2, pod, user_id,))
        bd.commit()
    elif user_stup[0][0] == 2:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =?, `user_blog_pod` =? WHERE `user_id` =?", (3, pod, user_id,))
        bd.commit()
    if user[0][0] == "Спорт":
        if pod == "pod1":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/tnsport/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod2":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/around_sports/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod3":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/trends/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod4":
            otvet = keyboard_sport_pod4("https://tengrinews.kz/champions-league/news/")
            return otvet
        elif pod == "pod5":
            otvet = keyboard_sport_pod5("https://tengrinews.kz/trends/")
            return otvet

    elif user[0][0] == "Вокруг мира":
        if pod == "pod1":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/my-country/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod2":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/around-the-world/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod3":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/travel-notes/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod5":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/sayakhat-time/", user_stup[0][0] + 1, user_id)
            return otvet

    elif user[0][0] == "Жизнь":
        if pod == "pod1":
            otvet = keyboard_life_pod1("https://tengrinews.kz/handsomely/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod2":
            otvet = keyboard_life_pod1("https://tengrinews.kz/profitably/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod3":
            otvet = keyboard_life_pod1("https://tengrinews.kz/healthy/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod4":
            otvet = keyboard_life_pod1("https://tengrinews.kz/curious/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod == "pod5":
            otvet = keyboard_life_pod1("https://tengrinews.kz/horoscopes/", user_stup[0][0] + 1, user_id)
            return otvet

def podkat2(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi_pod` WHERE `user_id` =?", (user_id,)).fetchall()
    pod = cursor.execute("SELECT `user_blog_pod` FROM `blogi_pod` WHERE `user_id` =?",(user_id,)).fetchall()
    if user_stup[0][0] == 0:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (1, user_id,))
        bd.commit()
    elif user_stup[0][0] == 1:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (2, user_id,))
        bd.commit()
    elif user_stup[0][0] == 2:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (3, user_id,))
        bd.commit()
    if user[0][0] == "Спорт":
        if pod[0][0] == "pod1":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/tnsport/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/around_sports/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/trends/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_sport_pod4("https://tengrinews.kz/champions-league/news/")
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_sport_pod5("https://tengrinews.kz/trends/")
            return otvet

    elif user[0][0] == "Вокруг мира":
        if pod[0][0] == "pod1":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/my-country/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/around-the-world/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/travel-notes/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/sayakhat-time/", user_stup[0][0] + 1, user_id)
            return otvet

    elif user[0][0] == "Жизнь":
        if pod[0][0] == "pod1":
            otvet = keyboard_life_pod1("https://tengrinews.kz/handsomely/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_life_pod1("https://tengrinews.kz/profitably/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_life_pod1("https://tengrinews.kz/healthy/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_life_pod1("https://tengrinews.kz/curious/", user_stup[0][0] + 1, user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_life_pod1("https://tengrinews.kz/horoscopes/", user_stup[0][0] + 1, user_id)
            return otvet

def povtor_novosti_pod(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi_pod` WHERE `user_id` =?", (user_id,)).fetchall()
    pod = cursor.execute("SELECT `user_blog_pod` FROM `blogi_pod` WHERE `user_id` =?",(user_id,)).fetchall()
    if user[0][0] == "Спорт":
        if pod[0][0] == "pod1":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/tnsport/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/around_sports/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/trends/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_sport_pod4("https://tengrinews.kz/champions-league/news/")
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_sport_pod5("https://tengrinews.kz/trends/")
            return otvet

    elif user[0][0] == "Вокруг мира":
        if pod[0][0] == "pod1":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/my-country/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/around-the-world/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/travel-notes/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/sayakhat-time/", user_stup[0][0], user_id)
            return otvet

    elif user[0][0] == "Жизнь":
        if pod[0][0] == "pod1":
            otvet = keyboard_life_pod1("https://tengrinews.kz/handsomely/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_life_pod1("https://tengrinews.kz/profitably/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_life_pod1("https://tengrinews.kz/healthy/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_life_pod1("https://tengrinews.kz/curious/", user_stup[0][0], user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_life_pod1("https://tengrinews.kz/horoscopes/", user_stup[0][0], user_id)
            return otvet

def all_kat(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    if user_stup[0][0] == 0:
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (1,user_id,))
        bd.commit()
    elif user_stup[0][0] == 1:
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (2,user_id,))
        bd.commit()
    elif user_stup[0][0] == 2:
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (3,user_id,))
        bd.commit()
    if user[0][0] == "Спорт":
        otvet = all_keyboard_sport(user_stup[0][0] + 1, user_id)
        return otvet
    elif user[0][0] == "Вокруг мира":
        otvet = all_keyboard_travel(user_stup[0][0] + 1, user_id)
        return otvet
    elif user[0][0] == "Жизнь":
        otvet = all_keyboard_life(user_stup[0][0] + 1, user_id)
        return otvet

    elif user[0][0] == "Узнай":
        otvet = novosti_yznai_pochitai_posmotri("Узнай", user_stup[0][0] + 1, user_id)
        return otvet
    elif user[0][0] == "Почитай":
        otvet = novosti_yznai_pochitai_posmotri("Почитай", user_stup[0][0] + 1, user_id)
        return otvet
    elif user[0][0] == "Посмотри":
        otvet = novosti_yznai_pochitai_posmotri("Посмотри", user_stup[0][0] + 1, user_id)
        return otvet

def povtor_novosti(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    if user[0][0] == "Спорт":
        otvet = all_keyboard_sport(user_stup[0][0], user_id)
        return otvet
    elif user[0][0] == "Вокруг мира":
        otvet = all_keyboard_travel(user_stup[0][0], user_id)
        return otvet
    elif user[0][0] == "Жизнь":
        otvet = all_keyboard_life(user_stup[0][0], user_id)
        return otvet

    elif user[0][0] == "Узнай":
        otvet = novosti_yznai_pochitai_posmotri("Узнай", user_stup[0][0], user_id)
        return otvet
    elif user[0][0] == "Почитай":
        otvet = novosti_yznai_pochitai_posmotri("Почитай", user_stup[0][0], user_id)
        return otvet
    elif user[0][0] == "Посмотри":
        otvet = novosti_yznai_pochitai_posmotri("Посмотри", user_stup[0][0], user_id)
        return otvet


def all_kat_nazad(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    if user_stup[0][0] == 3:
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (2, user_id,))
        bd.commit()
    elif user_stup[0][0] == 2:
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (1, user_id,))
        bd.commit()
    if user[0][0] == "Спорт":
        otvet = all_keyboard_sport(user_stup[0][0] - 1, user_id)
        return otvet
    elif user[0][0] == "Вокруг мира":
        otvet = all_keyboard_travel(user_stup[0][0] - 1,user_id)
        return otvet
    elif user[0][0] == "Жизнь":
        otvet = all_keyboard_life(user_stup[0][0] - 1, user_id)
        return otvet

    elif user[0][0] == "Узнай":
        otvet = novosti_yznai_pochitai_posmotri("Узнай", user_stup[0][0] - 1, user_id)
        return otvet
    elif user[0][0] == "Почитай":
        otvet = novosti_yznai_pochitai_posmotri("Почитай", user_stup[0][0] - 1, user_id)
        return otvet
    elif user[0][0] == "Посмотри":
        otvet = novosti_yznai_pochitai_posmotri("Посмотри", user_stup[0][0] - 1, user_id)
        return otvet

def podkat_nazad(user_id):
    user = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?", (user_id,)).fetchall()
    user_stup = cursor.execute("SELECT `stup` FROM `blogi_pod` WHERE `user_id` =?", (user_id,)).fetchall()
    pod = cursor.execute("SELECT `user_blog_pod` FROM `blogi_pod` WHERE `user_id` =?",(user_id,)).fetchall()
    if user_stup[0][0] == 3:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (2, user_id,))
        bd.commit()
    elif user_stup[0][0] == 2:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (1, user_id,))
        bd.commit()
    elif user_stup[0][0] == 1:
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (0, user_id,))
        bd.commit()
    if user[0][0] == "Спорт":
        if pod[0][0] == "pod1":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/tnsport/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/around_sports/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_sport_pod1("https://tengrinews.kz/trends/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_sport_pod4("https://tengrinews.kz/champions-league/news/")
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_sport_pod5("https://tengrinews.kz/trends/")
            return otvet

    elif user[0][0] == "Вокруг мира":
        if pod[0][0] == "pod1":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/my-country/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/around-the-world/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/travel-notes/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_travel_pod1("https://tengritravel.kz/sayakhat-time/", user_stup[0][0] - 1, user_id)
            return otvet

    elif user[0][0] == "Жизнь":
        if pod[0][0] == "pod1":
            otvet = keyboard_life_pod1("https://tengrinews.kz/handsomely/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod2":
            otvet = keyboard_life_pod1("https://tengrinews.kz/profitably/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod3":
            otvet = keyboard_life_pod1("https://tengrinews.kz/healthy/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod4":
            otvet = keyboard_life_pod1("https://tengrinews.kz/curious/", user_stup[0][0] - 1, user_id)
            return otvet
        elif pod[0][0] == "pod5":
            otvet = keyboard_life_pod1("https://tengrinews.kz/horoscopes/", user_stup[0][0] - 1, user_id)
            return otvet

def news(user_id,btn):
    links = cursor.execute("SELECT `nov_link1`,`nov_link2`,`nov_link3`,`nov_link4` FROM `parser_novosti` WHERE `user_id` =? ",(user_id,)).fetchall()
    user_blog = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?",(user_id,)).fetchall()
    if user_blog[0][0] == "Жизнь":
        otvet_parser = Life(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Спорт":
        otvet_parser = Sport(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Вокруг мира":
        otvet_parser = Travel(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Узнай":
        otvet_parser = Yznai(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Посмотри":
        otvet_parser = Posmotri(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Почитай":
        otvet_parser = Pochitai(links[0][btn])
        return otvet_parser

def news_pod(user_id,btn):
    links = cursor.execute("SELECT `nov_link1`,`nov_link2`,`nov_link3`,`nov_link4` FROM `parser_novosti_pod` WHERE `user_id` =? ",(user_id,)).fetchall()
    user_blog = cursor.execute("SELECT `user_blog` FROM `blogi` WHERE `user_id` =?",(user_id,)).fetchall()
    if user_blog[0][0] == "Жизнь":
        otvet_parser = Life(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Спорт":
        otvet_parser = Sport(links[0][btn])
        return otvet_parser
    elif user_blog[0][0] == "Вокруг мира":
        otvet_parser = Travel(links[0][btn])
        return otvet_parser