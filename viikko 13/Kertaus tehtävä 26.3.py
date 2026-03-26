#tehtava 1

numero = int(input("Anna numero väliltä 1-10:"))
for i in range(1,11):
    print(numero * i)

#tehtava 2

numero = int(input("Anna luku"))

lista = []

while numero !=0:
    lista.append(numero)
    print(lista)
    print("lisäysjärjestyksessä:", lista)
    print("lista pienimmästä suurimpaan:", sorted(lista))
    numero = int(input("Anna luku:"))

#tehtava 3

sanat = ["omena", "kirsikka", "vadelma","päärynä", "mansikka"]

yli_viisi = 0

for sana in sanat:
    if len(sana) > 5:
        yli_viisi += 1

print("sanoja joissa yli 5 kirjainta:", yli_viisi)


#tehtava 4

def kuusi(koko):
    print("Tämä on kuusi!")
    for i in range(1, koko + 1):

        print( " " * (koko - i) + "*" * (2*i-1))

kuusi(5)


#tehtava 5

def suurin_arvo(a,b,c):
    return max(a,b,c)

luku1 = int(input("Anna ensimmäinen luku:"))
luku2 = int(input("Anna toinen luku:"))
luku3 = int(input("Anna kolmas luku:"))

tulos = suurin_arvo(luku1, luku2, luku3)
print("Suurin arvo on:", tulos)

#tehtava 6

def summa (luku1, luku2):
    return luku1 + luku2

def erotus (luku1, luku2):
    return luku1 - luku2

def tulo (luku1, luku2):
    return luku1 * luku2

def jako (luku1, luku2):
    return luku1 / luku2




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
        tulos = summa(luku1, luku2)
        print(f"Tulos: {luku1} + {luku2} = {tulos} ")
    elif valinta == "2":
        tulos = erotus(luku1, luku2)
        print(f"Tulos: {luku1} - {luku2} = {tulos} ")
    elif valinta == "3":
        tulos = tulo(luku1, luku2)
        print(f"Tulos: {luku1} * {luku2} = {tulos}")
    elif valinta == "4":
        if luku2 == 0:
            print("Virhe: Nolalla ei voi jakaa!")
        else:
            tulos = jako(luku1, luku2)
            print(f"Tulos: {luku1} / {luku2} = {tulos} ")
else:
    print("Virheellinen valinta, yritä uudelleen. ")












