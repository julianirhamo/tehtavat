#tehtava 1


vuodenajat = (
    "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi",
)

vuodenaika = int(input("anna järjestysnumero, jonka vuodenajan haluat tarkistaa (1-12):"))

Vuodenaika = vuodenajat[vuodenaika-1]

print("numeroa vastaava kuukausi on", Vuodenaika)


#tehtava 2

nimet = set()

while True:
    nimi = input("anna nimi:")

    if nimi == "":
        break

    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)

print("syötetyt nimet:")

for nimi in nimet:
    print(nimi)

#tehtava 3

lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (uusi/ haku / lopeta):")

    if toiminto == "lopeta":
       break

    elif toiminto == "uusi":
        icao = input("anna lentoaseman ICAO-koodi:")
        nimi = input("anna lentoaseman nimi:")
        lentoasemat[icao] = nimi

    elif toiminto == "haku":
      icao = input("anna ICAO-koodi:")

      if icao in lentoasemat:
          print("lentoaseman nimi on:", lentoasemat[icao])

      else:
          print("lentoasemaa ei löytynyt")

    else:
        print("virheellinen toiminto")
