import requests
from bs4 import BeautifulSoup as bs

# Tengri Life
def Tengri_Life(link):
    s = f"{link}"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h3", class_="post-title")
    all_link = []
    all_text = []
    for i in find_:
        teg_a = i.find("a")
        link = teg_a.get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
        text = teg_a.text
        all_text.append(text)
    return all_text, all_link

def All_life():
    s = f"https://tengrinews.kz/mixnews/"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h3", class_="post-title")
    all_link = []
    all_text = []
    for i in find_:
        teg_a = i.findChildren("a")
        text_news = teg_a[0].text
        link = teg_a[0].get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
        all_text.append(text_news)
    for i3 in range(len(all_text)): # удаление лишних объектов в списке
        vrem = all_text[0]
        all_text.pop(0)
        itog = vrem in all_text
        if itog == False:
            all_text.append(vrem)
    for i3 in range(len(all_link)):
        vrem = all_link[0]
        all_link.pop(0)
        itog = vrem in all_link
        if itog == False:
            all_link.append(vrem)
    return all_text, all_link


# Tengri Sport
def Tengri_Sport(link):
    s = f"{link}"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("a", class_="media__text-link")
    all_link = []
    all_text = []
    for i in find_:
        link = i.get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
        text = i.text
        all_text.append(text)

    return all_text,all_link

# Tengri Sport_league
def Tengri_Sport_league(link):
    s = f"{link}"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("span", class_="title")
    find_2 = obr.find_all("div", class_="news_rubric_list_item")
    all_link = []
    all_text = []
    for i in find_2:
        find_link = i.findChildren("a")
        link_news = find_link[0].get("href")
        if "https" in link_news or "http" in link_news:
            all_link.append(link_news)
        else:
            abc = "https://tengrinews.kz/" + link_news
            all_link.append(abc)
    for i2 in find_:
        text_news = i2.text
        all_text.append(text_news)
    return all_text,all_link

def All_sport():
    s = f"https://tengrinews.kz/tengri-sport/"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("a", class_="media__text-link")
    all_link = []
    all_text = []
    for i in find_:
        text_news = i.text
        all_text.append(text_news)
        link = i.get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
    return all_text, all_link


# Tengri Travel
def Tengri_Travel(link):
    s = f"{link}"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h2", class_="entry-title")
    all_link = []
    all_text = []
    for i in find_:
        teg_a = i.find("a")
        link = teg_a.get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
        text = teg_a.text
        all_text.append(text)

    return all_text,all_link

def All_travel():
    s = f"https://tengritravel.kz"
    req = requests.get(s)
    obr = bs(req.text, "html.parser")
    find_ = obr.find_all("h2", class_="entry-title")
    all_link = []
    all_text = []
    for i in find_:
        teg_a = i.findChildren("a")
        text_news = teg_a[0].text
        link = teg_a[0].get("href")
        if "https" in link or "http" in link:
            all_link.append(link)
        else:
            abc = "https://tengrinews.kz/" + link
            all_link.append(abc)
        all_text.append(text_news)
    return all_text, all_link


# Tengri Посмотри, узнай, почитай
def Tengri_Posmotri_pochitai_yznai(kat):
    s = ""
    all_link = []
    all_text = []
    for c in range(1, 3):
        if kat == "Узнай":
            s = f"https://tengrinews.kz/find-out/page/{c}/"
        elif kat == "Почитай":
            s = f"https://tengrinews.kz/read/page/{c}/"
        elif kat == "Посмотри":
            s = f"https://tengrinews.kz/take-look/page/{c}/"
        req = requests.get(s)
        obr = bs(req.text, "html.parser")
        find_ = obr.find_all("a", class_="tn-link")
        for i in find_:
            link = i.get("href")
            if "https" in link or "http" in link:
                all_link.append(link)
            else:
                abc = "https://tengrinews.kz/" + link
                all_link.append(abc)
            text = i.text
            all_text.append(text)

    return all_text, all_link

