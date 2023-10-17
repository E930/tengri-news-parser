spisok = ["Автомобиль", "Самолёт", "Автомобиль", "Самолёт", "Мотоцикл"]
print(spisok)
for i in range(len(spisok)):
    vrem = spisok[0]
    spisok.pop(0)
    itog = vrem in spisok
    if itog == False:
        spisok.append(vrem)
print(spisok)


# spisok2 = ["Автомобиль", "Самолёт", "Автомобиль", "Самолёт", "Мотоцикл"]
# print(spisok2)
# for i2 in range(len(spisok2)):
