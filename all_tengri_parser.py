import requests
from bs4 import BeautifulSoup as bs

def all_parsers (link):
    try:
        # Узнай

        s = f"{link}"
        req = requests.get(s)
        obr = bs(req.text, "html.parser")
        find_ = obr.find_all("h1", class_="tn-content-title")
        find_[0].select_one("span").decompose()  # select_one("тэг").decompose() удаляет вложенный тэг
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

        return f"<b>{title}</b>", itog_text

    except:
        try:
            # Life

            s = f"{link}"
            req = requests.get(s)
            obr = bs(req.text, "html.parser")
            find_ = obr.find_all("h1", class_="post-title")
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

            return f"<b>{title}</b>", itog_text

        except:
            try:
                # Sport

                s = f"{link}"
                req = requests.get(s)
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

                return f"<b>{title}</b>", itog_text

            except:
                try:
                    # Travel

                    s = f"{link}"
                    req = requests.get(s)
                    obr = bs(req.text, "html.parser")
                    find_ = obr.find_all("h1", class_="entry-title")
                    title = find_[0].text + "\n"

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

                    return f"<b>{title}</b>", itog_text

                except:
                    try:
                        # Почитай

                        s = f"{link}"
                        req = requests.get(s)
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

                        return f"<b>{title}</b>", itog_text

                    except:
                        try:
                            # Посмотри

                            s = f"{link}"
                            req = requests.get(s)
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

                            return f"<b>{title}</b>", itog_text

                        except:
                            try:
                                req = requests.get(link)
                                obr = bs(req.text, "html.parser")
                                find_ = obr.find_all("div", class_="header")
                                title = find_[0].findChildren("h1")[0].text

                                find_2 = obr.find_all("div", class_="content")
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
                            except:
                                return f"Не удалось вывести <a href = '{link}'> статью </a>"