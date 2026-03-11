#tehtava 1

import random

kuutiot = int(input("Kuinka monta arpakuutiota heitetään?"))

summa = 0

for i in range(kuutiot):
    heitto = random.randint(1,6)
    summa = summa + heitto

print( "Silmälukujen summa on:", summa)

#tehtava 2

luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa):")

    if syote == "":
        break

    luvut.append(float(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut [:5]:
    print(luku)

#tehtava 3

luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    alkuluku = True

    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")

#tehtava 4

kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi:")
    kaupungit.append(nimi)

print("Kaupungit:")

for kaupunki in kaupungit:
    print(kaupunki)

