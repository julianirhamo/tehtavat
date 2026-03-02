#teht 1

luku = 1

while luku <= 1000:
    if luku %3 == 0:
        print(luku)
    luku += 1

#teht 2

while True:
    tuumat = float(input( "Anna tuumat (negatiivinen luku lopettaa): "))

    if tuumat < 0:
        print("Ohjelma loppuu.")
        break
    senttimetrit = tuumat * 2.54
    print("Senttimetreinä:", senttimetrit)

#teht 3

luvut = []

while True:
    syote = input("Anna luku(Enter lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")
        continue
    luvut.append(luku)

if luvut:
    print("Pieni luku:" , min(luvut))
    print("Suuri luku:", max(luvut))
else:
    print( "Et syöttänyt lukua.")

#teht 4

import random

# Tietokone arpoo luvun kerran
salainen_luku = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

    if arvaus < salainen_luku:
        print("Liian pieni arvaus ")
    elif arvaus > salainen_luku:
        print("Liian suuri arvaus ")
    else:
        print("Oikein ")
        break

#teht 5

oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
onnistui = False

while yritykset < 5:
    tunnus = input("Käyttäjätunnus:")
    salasana = input("Salasana:")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
      onnistui = True
      break
    else:
     print("Väärä tunnus tai salasana")
     yritykset += 1

if onnistui:
    print("Tervetuloa")
else:
    print("Pääsy evätty")







