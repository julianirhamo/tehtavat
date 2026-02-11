import math
r= float(input("Anna ympyrän säde"))
a= math.pi*r**2
print("Ympyrän pinta-ala on,",a)
kanta= float(input("Anna suorakulmion kanta: "))
korkeus= float(input("Anna suorakulmion korkeus: "))
print(f"Suorakulmion piiri on {kanta*2+korkeus*2}")
print(f"Suorakulmion pinta-ala on {kanta*korkeus}")
a= int(input("Anna eka luku: "))
b= int(input("Anna toka luku: "))
c= int(input("Anna kolmas luku:"))
print(f"Lukujen summa on {a+b+c}")
print(f"Lukujen tulo on {a*b*c}")
print(f"Lukujen keskiarvo on {(a+b+c)/3}")
leviskat= float(input("Anna leviskat: "))
naulat= float(input("Anna naulat: "))
luodit= float(input("Anna luodit: "))
luoti_grammoina= 13.3
naula_grammoina= 32*luoti_grammoina
leviska_grammoina= 20*naula_grammoina
massa_grammoina= (leviskat*leviska_grammoina+naulat*naula_grammoina+luodit*luoti_grammoina)
kilot= int(massa_grammoina//1000)
grammat= massa_grammoina%1000
print(f"{kilot}kilogrammaa ja {grammat}grammaa")
