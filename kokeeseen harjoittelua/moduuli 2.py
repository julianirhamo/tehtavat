print("Hei, Julia!")

#moduuli 2

nimi = input("Mikä on sinun nimesi?")

print("Terve," + nimi + "!")

import math

sade = float(input(" Mikä on ympyrän säde: "))
pinta_ala = math.pi * sade ** 2

print("Ympyrän pinta-ala on:", pinta_ala)

import math

kanta = float(input("Mikä on suorakulmion kanta:"))
korkeus = float(input("Mikä on suorakulmion korkeus:"))

pinta_ala = kanta * korkeus

piiri = 2* kanta + 2*korkeus

print("Suorakulmion pinta-ala on:", pinta_ala)
print("Suorakulmion piiri on:", piiri)

import math

luku1 = int(input("anna kokonaisluku:"))
luku2 = int(input("anna toinen kokonaisluku:"))
luku3 = int(input("anna kolmas kokonaisluku:"))

summa = luku1 + luku2 +luku3

tulo = luku1 * luku2 * luku3

keskiarvo = summa / 3

print("Summa:", summa)
print("Tulo:", tulo)
print("Keskiarvo:", keskiarvo)


import math

leviskat = int(input("anna leviskät:"))
naulat = int(input("anna naulat:"))
luodit = float(input("anna luodit:"))

luodit_yhteensa = leviskat * 20 * 32 + naulat * 32 + luodit

grammat = (luodit_yhteensa *13.3)

kilot = int(grammat // 1000)

grammat_jaljella = grammat % 1000

print(kilot, "kilogrammaa ja", grammat_jaljella, "grammaa")
