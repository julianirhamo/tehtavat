#teht 1

nimi = input("Anna nimesi: ")

if nimi != "Matti":
    maara = int(input("kuninka monta annosta haluat keittoa? "))
    hinta_per_annos = 5.90
    kokonaishinta = maara * hinta_per_annos
    print("Kokonaishinta on", round(kokonaishinta, 2), "euroa.")
else:
    print("Matti saa keiton ilmaiseksi!")

#teht 2

tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
paiva = input("Anna viikonpäivä: ")

if paiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print("Päiväpalkka on", round(paivapalkka, 2), "euroa.")

#tehtava 3
import math

while True:
    luku = int(input("Anna kokonaisluku (0 lopettaa): "))

    if luku < 0:
        print("Virheellinen numero")
    elif luku > 0:
        juuri = math.sqrt(luku)
        print("Luvun neliöjuuri on", juuri)
    else:
        print("Luku on 0, neliöjuuri on 0")

    if luku == 0:
        print("Ohjelma lopetetaan. ")
        break

#teht 4

tarina = ""

while True:
    sana = input("Anna sana(kirjoita 'loppu' lopettaaksesi):")

    if sana == "loppu":
        print("Muodostunut tarina:")
        print(tarina)
        break
    else:
        tarina += sana + " "

#teht 5

while True:
    print("Valitse laskutoimitus:")
    print("1 - Yhteenlasku")
    print("2 - Vähennyslasku")
    print("3 - Kertolasku")
    print("4 - Jakolasku")
    print("5 - Lopeta ohjelma")

    valinta = input("Syötä valintasi(1-5):")

    if valinta == "5":
        print("Ohjelma lopetetaan. Hei hei!")
        break

    if valinta in ["1", "2", "3", "4"]:
        try:
            luku1 = float(input("Anna ensimmäinen luku: "))
            luku2 = float(input("Anna toinen luku: "))
        except ValueError:
            print("Virhe: syötä numerot!")
            continue

    if valinta == "1":
        tulos = luku1 + luku2
        print(f"Tulos: {luku1} + {luku2} = {tulos} ")
    elif valinta == "2":
        tulos = luku1 - luku2
        print(f"Tulos: {luku1} - {luku2} = {tulos} ")
    elif valinta == "3":
        tulos = luku1 * luku2
        print(f"Tulos: {luku1} * {luku2} = {tulos}")
    elif valinta == "4":
        if luku2 == 0:
            print("Virhe: Nolalla ei voi jakaa!")
        else:
            tulos = luku1 / luku2
            print(f"Tulos: {luku1} / {luku2} = {tulos} ")
else:
    print("Virheellinen valinta, yritä uudelleen. ")




