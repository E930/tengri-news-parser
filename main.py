import logging
from aiogram import Bot,Dispatcher,executor,types
from config import TOKEN
import sqlite3
from bd import *
from inline_keyboard import *
from parser_tengri import *
from math import *

bd = sqlite3.connect("tengri.db")
cursor = bd.cursor()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start (message:types.Message):
    await bot.send_message(message.chat.id, "Выберите категорию", reply_markup=start_inline())


@dp.callback_query_handler(lambda stat:stat.data)
async def tekst (call):
    user_id = call.from_user.id
    if call.data == "btn1":
        otvet = bd_tengri(user_id,"Узнай")
        novosti = all_kat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=novosti, parse_mode="html")
    elif call.data == "btn5":
        otvet = bd_tengri(user_id, "Почитай")
        novosti = all_kat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=novosti, parse_mode="html")
    elif call.data == "btn6":
        otvet = bd_tengri(user_id, "Посмотри")
        novosti = all_kat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=novosti, parse_mode="html")

    elif call.data == "btn2":
        otvet = bd_tengri(user_id, "Жизнь")
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=choice(), parse_mode="html")
    elif call.data == "btn3":
        otvet = bd_tengri(user_id, "Спорт")
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=choice(), parse_mode="html")
    elif call.data == "btn4":
        otvet = bd_tengri(user_id, "Вокруг мира")
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{otvet}",
                                    reply_markup=choice(), parse_mode="html")


    elif call.data == "pod1":
        otvet = podkat1(user_id,"pod1")
        await bot.send_message(call.message.chat.id, "Список новостей", reply_markup=otvet)
    elif call.data == "pod2":
        otvet = podkat1(user_id,"pod2")
        await bot.send_message(call.message.chat.id, "Список новостей", reply_markup=otvet)
    elif call.data == "pod3":
        otvet = podkat1(user_id,"pod3")
        await bot.send_message(call.message.chat.id, "Список новостей", reply_markup=otvet)
    elif call.data == "pod4":
        otvet = podkat1(user_id,"pod4")
        await bot.send_message(call.message.chat.id, "Список новостей", reply_markup=otvet)
    elif call.data == "pod5":
        otvet = podkat1(user_id,"pod5")
        await bot.send_message(call.message.chat.id, "Список новостей", reply_markup=otvet)


    elif call.data == "nov1":
        otvet = news(user_id, 0)
        kolvo_sym = len(otvet[1])
        if kolvo_sym <= 3500:
            await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1],disable_web_page_preview=True, parse_mode="html")
        elif kolvo_sym <= 7000:
            try:
                await bot.send_message(call.message.chat.id, otvet[1][0:3500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][3500:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
            except:
                await bot.send_message(call.message.chat.id, otvet[1][0:4000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][4000:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
        elif kolvo_sym <= 10500:
            try:
                await bot.send_message(call.message.chat.id, otvet[1][0:3500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][3500:7000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7000:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
            except:
                await bot.send_message(call.message.chat.id, otvet[1][0:4000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][4000:7500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7500:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
        elif kolvo_sym <= 14000:
            try:
                await bot.send_message(call.message.chat.id, otvet[1][0:3500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][3500:7000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7000:10500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][10500:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
            except:
                await bot.send_message(call.message.chat.id, otvet[1][0:4000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][4000:7500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7500:11000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][11000:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
        elif kolvo_sym <= 17500:
            try:
                await bot.send_message(call.message.chat.id, otvet[1][0:3500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][3500:7000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7000:10500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][10500:14000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][14000:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
            except:
                await bot.send_message(call.message.chat.id, otvet[1][0:4000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][4000:7500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7500:11000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][11000:14500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][14500:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
        elif kolvo_sym <= 21000:
            try:
                await bot.send_message(call.message.chat.id, otvet[1][0:3500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][3500:7000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7000:10500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][10500:14000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][14000:17500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][17500:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
            except:
                await bot.send_message(call.message.chat.id, otvet[1][0:4000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][4000:7500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][7500:11000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][11000:14500], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][14500:18000], disable_web_page_preview=True, parse_mode="html")
                await bot.send_message(call.message.chat.id, otvet[1][18000:kolvo_sym], disable_web_page_preview=True, parse_mode="html")
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov2":
        otvet = news(user_id, 1)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                else:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov3":
        otvet = news(user_id, 2)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                else:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov4":
        otvet = news(user_id, 3)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                else:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)

    elif call.data == "nov_pod1":
        otvet = news_pod(user_id,0)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                else:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+3500],disable_web_page_preview=True, parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x+4000],disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov_pod2":
        otvet = news_pod(user_id,1)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 3500],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    await bot.send_message(call.message.chat.id, otvet[1][x:x + 3500], disable_web_page_preview=True,
                                           parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 4000],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x + 4000],
                                               disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov_pod3":
        otvet = news_pod(user_id,2)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 3500],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    await bot.send_message(call.message.chat.id, otvet[1][x:x + 3500], disable_web_page_preview=True,
                                           parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 4000],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x + 4000],
                                               disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)
    elif call.data == "nov_pod4":
        otvet = news_pod(user_id,3)
        kolvo_sym = ceil(len(otvet[1])/3500)
        x = 0
        for i in range(kolvo_sym):
            try:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 3500],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    await bot.send_message(call.message.chat.id, otvet[1][x:x + 3500], disable_web_page_preview=True,
                                           parse_mode="html")
                x += 3500
            except:
                if i == 0:
                    await bot.send_message(call.message.chat.id, otvet[0] + "\n" + otvet[1][x:x + 4000],
                                           disable_web_page_preview=True, parse_mode="html")
                else:
                    try:
                        await bot.send_message(call.message.chat.id, otvet[1][x:x + 4000],
                                               disable_web_page_preview=True, parse_mode="html")
                    except:
                        pass
                x += 4000
        await bot.send_message(call.message.chat.id, "Выберите новость", reply_markup=povtor_novosti_pod(user_id),
                               disable_web_page_preview=True)


    elif call.data == "nazad":
        cursor.execute("UPDATE `blogi` SET `stup` =? WHERE `user_id` =?", (0, user_id,))
        bd.commit()
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите категорию",
                                    reply_markup=start_inline(), parse_mode="html")

    elif call.data == "all_vpered":
        otvet_bd = all_kat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите новость", reply_markup=otvet_bd, parse_mode="html")
    elif call.data == "all_nazad":
        otvet_bd = all_kat_nazad(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите новость", reply_markup=otvet_bd, parse_mode="html")

    elif call.data == "nazad_pod":
        cursor.execute("UPDATE `blogi_pod` SET `stup` =? WHERE `user_id` =?", (0, user_id,))
        bd.commit()
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите категорию",
                                    reply_markup=start_inline(), parse_mode="html")
    elif call.data == "all_vpered_pod":
        otvet_bd = podkat2(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите новость", reply_markup=otvet_bd, parse_mode="html")
    elif call.data == "all_nazad_pod":
        otvet_bd = podkat_nazad(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите новость", reply_markup=otvet_bd, parse_mode="html")

    elif call.data == "choice_kat":
        otvet_bd = podkat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите подкатегорию",reply_markup=otvet_bd, parse_mode="html")
    elif call.data == "all_kat":
        otvet_bd = all_kat(user_id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Выберите новость", reply_markup=otvet_bd, parse_mode="html")







if __name__ == '__main__':
    cursor.execute("UPDATE `blogi` SET `stup` =? ", (0,))
    bd.commit()
    cursor.execute("UPDATE `blogi_pod` SET `stup` =? ", (0,))
    bd.commit()
    executor.start_polling(dp)