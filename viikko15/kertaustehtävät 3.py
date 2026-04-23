#tehtava 1

tiedot = {"John" :["John", 30, "Engineering"],
          "Emily" : ["Emily", 25, "Artist"],
          "Anna" : ["Anna", 22, "Student"]}

print(tiedot["John"] [0])
print(tiedot["John"] [1])
print(tiedot["Emily"] [2])

tiedot["Anna"][2] = "Teacher"
tiedot["James"] = ["James", 28, "writer"]

tiedot["Sophia"] = ["Sophia", 35, "Doctor"]
del tiedot["Emily"]

print("Lopullinen sanakirja:")

for i in tiedot:
    print(tiedot[i])

#tehtava 2

oppilaat = {
    "Maija": ["Maija", 4, "Matikka"],
    "Keijo": ["Keijo", 4, "Historia"],
    "Pirjo": ["Pirjo", 3, "Fysiikka"],
    "Tiina": ["Tiina", 3, "Liikunta"]
}

print(oppilaat["Maija"][1])
print(oppilaat["Keijo"][2])

oppilaat["Pirjo"][2] = "Englanti"
oppilaat["Tiitu"] = ["Tiitu", 3, "Äidinkieli"]
del oppilaat["Tiina"]

print("Uusi päivitetty sanakirja:")

for i in oppilaat:
    print(oppilaat[i])

#tehtavat 3

kirjasto = {
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Sota"],
    "Seitsemän veljestä": ["Aleksis Kivi", 1870, "Klassikko"],
    "Risto Räppääjä": ["Sinikka Nopola", 1997, "Lasten kirja"],
    "Puhdistus": ["Sofi Oksanen", 2008, "Draama"]
}
print(kirjasto["Tuntematon sotilas"][0])
print(kirjasto["Seitsemän veljestä"][2])

kirjasto["Risto Räppääjä"][2] = "Jännitys"
kirjasto["Kalevala"] = ["Elias Lönnrot", 1835, "Eepos"]
del kirjasto["Tuntematon sotilas"]

print("Tässä päivitetty sanakirja:")
for i in kirjasto:
    print(kirjasto[i])


#tehtava 4

import math

def create_point (x, y):
    return(x, y)

def distance (p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

x1 = float(input("anna x1:"))
y1 = float(input("anna y1:"))
x2 = float(input("anna x2:"))
y2 = float(input("anna y2:"))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

d = distance(p1, p2)

print(f"Etäisyys: {d:.2f}")


