#tehtava 1

pituus = float(input("anna kuhan pituus:"))

if pituus < 37:
    puuttuu = 31 - pituus
    print("kuha on liian pieni,päästä se pois")
    print("pituudesta puuttuu", puuttuu, "cm")

else:
    print("kuha on sallitun mittainen")


#tehtava 2

hyttiluokka = input("mikä on hyttyluokkasi:")

if hyttiluokka == "LUX":
    print("parvekkeellinen hytti yläkannella")

elif hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")

elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")

elif hyttiluokka == "C":
    print("ikkunaton hytti autokannen alapuolella")

else:
    print("virheellinen hyttiluokka")



#tehtava 3

sukupuoli = input("anna sukupuoli (nainen, mies):")
hemoglobiini = float(input("anna hemoglobiini arvosi:"))

if sukupuoli == "nainen" and hemoglobiini < 117:
    print("hemoglobiinisi on alhainen")

elif sukupuoli == "nainen" and hemoglobiini >175:
    print("hemoglobiinisi on korkea")

elif sukupuoli == "nainen" and hemoglobiini <=175:
    print("hemoglobiinisi on normaali")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiinisi on alhainen")
    elif hemoglobiini <= 195:
        print("hemoglobiinisi on normaali")
    else:
        print("hemoglobiinisi on korkea")

else:
    print("virheellinen sukupuoli")


#tehtava 4

vuosi = int(input("anna vuosiluku:"))

if vuosi %4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")
