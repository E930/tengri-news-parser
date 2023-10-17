import requests
from bs4 import BeautifulSoup as bs
from all_tengri_parser import *



# Life
# def Life(link):
#     req = requests.get(link)
#     obr = bs(req.text, "html.parser")
#     find_ = obr.find_all("h1", class_="post-title")
#     title = find_[0].text
#
#     find_2 = obr.find_all("div", class_="post-content")
#     text_news = find_2[0].findChildren("p")
#     itog_text = ""
#     for i in range(len(text_news)):
#         all_link = []
#         all_text_link = []
#         cord_x1 = []
#         cord_x2 = []
#         if " " in text_news[i].text:
#             teg_p = ""
#             if "Публикация от" in text_news[i].text:
#                 pass
#             else:
#                 teg_p += text_news[i].text
#                 if "Фото:" in teg_p:
#                     pass
#                 else:
#                     teg_a = text_news[i].findChildren("a")
#                     for i2 in range(len(teg_a)):
#                         link = teg_a[i2].get("href")
#                         if "https" in link or "http" in link:
#                                 all_link.append(link)
#                         else:
#                             abc = "https://tengrinews.kz/" + link
#                             all_link.append(abc)
#                         text = teg_a[i2].text
#                         all_text_link.append(text)
#                     for i3 in range(len(all_link)):
#                         x1 = teg_p.find(all_text_link[i3])
#                         x2 = x1 + len(all_text_link[i3])
#                         cord_x1.append(x1)
#                         cord_x2.append(x2)
#                     if len(all_text_link) == 0:
#                         itog_text += text_news[i].text + "\n" + "\n"
#                     elif len(all_text_link) == 1:
#                         itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
#                     elif len(all_text_link) == 2:
#                         itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
#                                      f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"
#
#     return title, itog_text

# Life
def Life(link):
    req = requests.get(link)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h1", class_="post-title")
    title = find_[0].text

    find_2 = obr.find_all("div", class_="post-content")
    text_news_ = find_2[0].findChildren("p")
    text_news = []
    itog_text = ""
    for y in range(len(text_news_)):
        public_ot = text_news_[y].text
        if "Публикация от" in public_ot:
            pass
        else:
            text_news.append(text_news_[y])

    for i in range(len(text_news)):
        all_link = []
        all_text_link = []
        cord_x1 = []
        cord_x2 = []
        if " " in text_news[i].text:
            teg_p = ""
            if "Публикация от" in text_news[i].text:
                pass
            else:
                teg_p += text_news[i].text
            if "Фото:" in teg_p:
                pass
            else:
                teg_a = text_news[i].findChildren("a")
                for i2 in range(len(teg_a)):
                    link = teg_a[i2].get("href")
                    if "https" in link or "http" in link:
                        all_link.append(link)
                    else:
                        abc = "https://tengrinews.kz/" + link
                        all_link.append(abc)
                    text = teg_a[i2].text
                    all_text_link.append(text)
                for i3 in range(len(all_link)):
                    x1 = teg_p.find(all_text_link[i3])
                    x2 = x1 + len(all_text_link[i3])
                    cord_x1.append(x1)
                    cord_x2.append(x2)
                if len(all_text_link) == 0:
                    itog_text += text_news[i].text + "\n" + "\n"
                elif len(all_text_link) == 1:
                    itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
                elif len(all_text_link) == 2:
                    itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                                 f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

    return title, itog_text

# Sport
def Sport(link):
    try:
        req = requests.get(link)
        obr = bs(req.text, "html.parser")
        find_ = obr.find_all("h1", class_="news__heading")
        title = find_[0].text

        find_2 = obr.find_all("div", class_="news__text")
        text_news = find_2[0].findChildren("p")
        itog_text = ""
        for i in range(len(text_news)):
            all_link = []
            all_text_link = []
            cord_x1 = []
            cord_x2 = []
            if " " in text_news[i].text:
                teg_p = text_news[i].text
                teg_a = text_news[i].findChildren("a")
                for i2 in range(len(teg_a)):
                    link = teg_a[i2].get("href")
                    if "https" in link or "http" in link:
                            all_link.append(link)
                    else:
                        abc = "https://tengrinews.kz/" + link
                        all_link.append(abc)
                    text = teg_a[i2].text
                    all_text_link.append(text)
                for i3 in range(len(all_link)):
                    x1 = teg_p.find(all_text_link[i3])
                    x2 = x1 + len(all_text_link[i3])
                    cord_x1.append(x1)
                    cord_x2.append(x2)
                if len(all_text_link) == 0:
                    itog_text += text_news[i].text + "\n" + "\n"
                elif len(all_link) == 1:
                    itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
                elif len(all_text_link) == 2:
                    itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                                 f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

        return title, itog_text
    except:
        otvet = all_parsers(link)
        return otvet


# Travel
def Travel(link):
    req = requests.get(link)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h1", class_="entry-title")
    title = find_[0].text

    find_2 = obr.find_all("div", class_="post-content")
    text_news = find_2[0].findChildren("p")
    itog_text = ""

    for i in range(len(text_news)):
        all_link = []
        all_text_link = []
        cord_x1 = []
        cord_x2 = []
        if " " in text_news[i].text:
            teg_p = text_news[i].text
            teg_a = text_news[i].findChildren("a")
            for i2 in range(len(teg_a)):
                link = teg_a[i2].get("href")
                if "https" in link or "http" in link:
                        all_link.append(link)
                else:
                    abc = "https://tengrinews.kz/" + link
                    all_link.append(abc)
                text = teg_a[i2].text
                all_text_link.append(text)
            for i3 in range(len(all_link)):
                x1 = teg_p.find(all_text_link[i3])
                x2 = x1 + len(all_text_link[i3])
                cord_x1.append(x1)
                cord_x2.append(x2)
            if len(all_text_link) == 0:
                itog_text += text_news[i].text + "\n" + "\n"
            elif len(all_text_link) == 1:
                itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
            elif len(all_text_link) == 2:
                itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                             f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

    return title, itog_text


# Узнай
def Yznai(link):
    try:
        req = requests.get(link)
        obr = bs(req.text, "html.parser")
        find_ = obr.find_all("h1", class_="tn-content-title")
        find_[0].select_one("span").decompose()  # select_one("тэг").decompose() удаляет вложенный тэг
        title = find_[0].text

        find_2 = obr.find_all("article", class_="tn-news-text")
        text_news = find_2[0].findChildren("p")
        itog_text = ""
        print(title)
        for i in range(len(text_news)):
            all_link = []
            all_text_link = []
            cord_x1 = []
            cord_x2 = []
            if " " in text_news[i].text:
                teg_p = text_news[i].text
                teg_a = text_news[i].findChildren("a")
                for i2 in range(len(teg_a)):
                    link = teg_a[i2].get("href")
                    if "https" in link or "http" in link:
                        all_link.append(link)
                    else:
                        abc = "https://tengrinews.kz/" + link
                        all_link.append(abc)
                    text = teg_a[i2].text
                    all_text_link.append(text)
                for i3 in range(len(all_link)):
                    x1 = teg_p.find(all_text_link[i3])
                    x2 = x1 + len(all_text_link[i3])
                    cord_x1.append(x1)
                    cord_x2.append(x2)
                if len(all_text_link) == 0:
                    itog_text += text_news[i].text + "\n" + "\n"
                elif len(all_text_link) == 1:
                    itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
                elif len(all_text_link) == 2:
                    itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                                 f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

        return title, itog_text
    except:
            otvet = all_parsers(link)
            return otvet


# Почитай
def Pochitai(link):
    req = requests.get(link)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h1", class_="tn-content-title")
    title = find_[0].text

    find_2 = obr.find_all("article", class_="tn-news-text")
    text_news = find_2[0].findChildren("p")
    itog_text = ""
    for i in range(len(text_news)):
        all_link = []
        all_text_link = []
        cord_x1 = []
        cord_x2 = []
        if " " in text_news[i].text:
            teg_p = text_news[i].text
            teg_a = text_news[i].findChildren("a")
            for i2 in range(len(teg_a)):
                link = teg_a[i2].get("href")
                if "https" in link or "http" in link:
                    all_link.append(link)
                else:
                    abc = "https://tengrinews.kz/" + link
                    all_link.append(abc)
                text = teg_a[i2].text
                all_text_link.append(text)
            for i3 in range(len(all_link)):
                x1 = teg_p.find(all_text_link[i3])
                x2 = x1 + len(all_text_link[i3])
                cord_x1.append(x1)
                cord_x2.append(x2)
            if len(all_text_link) == 0:
                itog_text += text_news[i].text + "\n" + "\n"
            elif len(all_text_link) == 1:
                itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
            elif len(all_text_link) == 2:
                itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                             f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

    return title, itog_text


# Посмотри
def Posmotri(link):
    req = requests.get(link)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h1", class_="tn-content-title")
    title = find_[0].text

    find_2 = obr.find_all("article", class_="tn-news-text")
    text_news = find_2[0].findChildren("p")
    itog_text = ""
    for i in range(len(text_news)):
        all_link = []
        all_text_link = []
        cord_x1 = []
        cord_x2 = []
        if " " in text_news[i].text:
            teg_p = text_news[i].text
            teg_a = text_news[i].findChildren("a")
            for i2 in range(len(teg_a)):
                link = teg_a[i2].get("href")
                if "https" in link or "http" in link:
                    all_link.append(link)
                else:
                    abc = "https://tengrinews.kz/" + link
                    all_link.append(abc)
                text = teg_a[i2].text
                all_text_link.append(text)
            for i3 in range(len(all_link)):
                x1 = teg_p.find(all_text_link[i3])
                x2 = x1 + len(all_text_link[i3])
                cord_x1.append(x1)
                cord_x2.append(x2)
            if len(all_text_link) == 0:
                itog_text += text_news[i].text + "\n" + "\n"
            elif len(all_text_link) == 1:
                itog_text += f"{teg_p[0:cord_x1[0]]}<a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:]}" + "\n\n"
            elif len(all_text_link) == 2:
                itog_text += f"{teg_p[0:cord_x1[0]]} <a href = '{all_link[0]}'>{all_text_link[0]}</a> {teg_p[cord_x2[0]:cord_x1[1]]}" \
                             f"<a href = '{all_link[1]}'>{all_text_link[1]}</a> {teg_p[cord_x2[1]:]}" + "\n\n"

    return title, itog_text