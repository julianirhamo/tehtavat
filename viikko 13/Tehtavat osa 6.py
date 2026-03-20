#tehtava 1

import random

def heita_noppaa():
    return random.randint(1,6)

while True:
    tulos = heita_noppaa()
    print("Heitto:",tulos)
    if tulos == 6:
        break

#tehtava 2

import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä:"))

while True:
    tulos = heita_noppaa(maksimi)
    print("Heitto:", tulos)
    if tulos == maksimi:
        break

#tehtava 3


def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    maara = float(input("Anna gallona määrä(negatiivinen lopettaa):"))
    if maara < 0:
        break
    litrat = gallonat_litroiksi(maara)
    print("Litraa:", litrat)

#tehtava 4

def laske_summa(lista):
    return sum(lista)

luvut = [1,2,3,4,5]
tulos = laske_summa(luvut)
print("Lista:", luvut)
print("Summa:", tulos)


#tehtava 5

def poista_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

luvut = [1,2,3,4,5,6,7]
karsittu = poista_parittomat(luvut)

print("Alkuperäinen:", luvut)
print("Karsittu:", karsittu)


#tehtava 6

import math

def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm/100)/2
    pinta_ala = math.pi * sade_m **2
    return hinta_euro / pinta_ala

h1 = float(input("Pizza 1 halkaisija (cm):"))
p1 = float(input("Pizza 1 hinta (€):"))

h2 = float(input("Pizza 2 halkaisija (cm):"))
p2 = float(input("Pizza 2 hinta (€):"))

y1 = pizzan_yksikkohinta(h1, p1)
y2 = pizzan_yksikkohinta(h2, p2)

print("Pizza 1 yksikköhinta:", y1)
print("Pizza 2 yksikköhinta:", y2)

if y1 < y2:
    print("Pizza 1 antaa paremman vastineen rahalle")
elif y2< y1:
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Pizzat ovat yhtä edullisia")



