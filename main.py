import fileinput


import numpy as np
figury = ["p", "w", "g", "s", "q", "k"]
pomoc = ["0", "1", "2", "3", "4", "5", "6", "7"]


def ruchy(kolor, rzad, kolumna, bierka):
    szachownica = np.array([
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
    ])

    if bierka not in figury:
        print("Blednie podana bierka!")
        exit()
    if rzad not in pomoc:
        print("Blednie podany rzad!")
        exit()
    if kolumna not in pomoc:
        print("Blednie podany rzad!")
        exit()
    rzad = int(rzad)
    kolumna = int(kolumna)
    if kolor == "b":
        szachownica[int(rzad)][kolumna] = bierka.upper()
    elif kolor == "c":
        szachownica[rzad][kolumna] = bierka.lower()
    else:
        print("Blednie podany kolor!")
        exit()

    if bierka == "p":
        if kolor == "c":
            if rzad - 1 < 0:
                print("Pion nie moze sie ruszyc!")
            else:
                szachownica[rzad - 1][kolumna] = "x"
        else:
            if rzad + 1 > 7:
                print("Pion nie moze sie ruszyc!")
            else:
                szachownica[rzad + 1][kolumna] = "x"
    elif bierka == "s":
        if rzad + 2 < 8 and kolumna + 1 < 8:
            szachownica[rzad + 2][kolumna + 1] = "x"
        if rzad + 2 < 8 and kolumna - 1 > -1:
            szachownica[rzad + 2][kolumna - 1] = "x"
        if rzad - 2 > -1 and kolumna + 1 < 8:
            szachownica[rzad - 2][kolumna + 1] = "x"
        if rzad - 2 > -1 and kolumna - 1 > -1:
            szachownica[rzad - 2][kolumna - 1] = "x"
        if rzad + 1 < 8 and kolumna + 2 < 8:
            szachownica[rzad + 1][kolumna + 2] = "x"
        if rzad + 1 < 8 and kolumna - 2 > - 1:
            szachownica[rzad + 1][kolumna - 2] = "x"
        if rzad - 1 > -1 and kolumna + 2 < 8:
            szachownica[rzad - 1][kolumna + 2] = "x"
        if rzad - 1 > -1 and kolumna - 2 > -1:
            szachownica[rzad - 1][kolumna - 2] = "x"
    elif bierka == "w":
        x = rzad
        y = kolumna
        while x > 0:
            szachownica[x - 1][y] = "x"
            x -= 1
        x = rzad
        while x < 7:
            szachownica[x + 1][y] = "x"
            x += 1
        x = rzad
        while y > 0:
            szachownica[x][y - 1] = "x"
            y -= 1
        y = kolumna
        while y < 7:
            szachownica[x][y + 1] = "x"
            y += 1
    elif bierka == "g":
        x = rzad
        y = kolumna
        while x > 0 and y > 0:
            szachownica[x - 1][y - 1] = "x"
            x -= 1
            y -= 1
        x = rzad
        y = kolumna
        while x > 0 and y < 7:
            szachownica[x - 1][y + 1] = "x"
            x -= 1
            y += 1
        x = rzad
        y = kolumna
        while x < 7 and y < 7:
            szachownica[x + 1][y + 1] = "x"
            x += 1
            y += 1
        x = rzad
        y = kolumna
        while x < 7 and y > 0:
            szachownica[x + 1][y - 1] = "x"
            x += 1
            y -= 1
    elif bierka == "q":
        x = rzad
        y = kolumna
        while x > 0:
            szachownica[x - 1][y] = "x"
            x -= 1
        x = rzad
        while x < 7:
            szachownica[x + 1][y] = "x"
            x += 1
        x = rzad
        while y > 0:
            szachownica[x][y - 1] = "x"
            y -= 1
        y = kolumna
        while y < 7:
            szachownica[x][y + 1] = "x"
            y += 1
        y = kolumna
        while x > 0 and y > 0:
            szachownica[x - 1][y - 1] = "x"
            x -= 1
            y -= 1
        x = rzad
        y = kolumna
        while x > 0 and y < 7:
            szachownica[x - 1][y + 1] = "x"
            x -= 1
            y += 1
        x = rzad
        y = kolumna
        while x < 7 and y < 7:
            szachownica[x + 1][y + 1] = "x"
            x += 1
            y += 1
        x = rzad
        y = kolumna
        while x < 7 and y > 0:
            szachownica[x + 1][y - 1] = "x"
            x += 1
            y -= 1
    elif bierka == "k":
        x = rzad
        y = kolumna
        if x > 0:
            szachownica[x - 1][y] = "x"
        if x < 7:
            szachownica[x + 1][y] = "x"
        if y > 0:
            szachownica[x][y - 1] = "x"
        if y < 7:
            szachownica[x][y + 1] = "x"
        if x > 0 and y > 0:
            szachownica[x - 1][y - 1] = "x"
        if x > 0 and y < 7:
            szachownica[x - 1][y + 1] = "x"
        if x < 7 and y < 7:
            szachownica[x + 1][y + 1] = "x"
        if x < 7 and y > 0:
            szachownica[x + 1][y - 1] = "x"
    print(szachownica)


file_pomoc = ""
for line in fileinput.input():
    file_pomoc += line
    file_pomoc += "\n"
f = open("przyklad.txt", "w")
f.write(file_pomoc)
try:
    kolor, rzad, kolumna, bierka = file_pomoc.split()
except:
    print("Bledna ilosc danych!")
    exit()

ruchy(kolor, rzad, kolumna, bierka)
f.close()

