#Lectia 7
#Comprehensiune
#Vreau sa creez o lista de 10 emelente de la 1 la 10
#Varianta clasica
#import numpy
'''
numere = []
for numar in range(1, 11):
    numere.append(numar)
print(numere)
#Varianta cu comprehensiune
numere = [x for x in range(1, 11) if x%2==0]
print(numere)
'''
#Astazi Pachete
#V1
import pachetulMeu.modul1 as m1
#V2
from pachetulMeu import modul2 as m2
import datetime

print(m1.mediaAritmetica(1,2))

m1.afisareNumerePrime(30)
print()
print(m1.generareMatrice(4, 4))
#Task 4
print(datetime.date.today())
print(datetime.date.today().strftime("%A"))
print("Today is " + datetime.date.today().strftime("%A") + " " + datetime.date.today().strftime("%j"))
print("This month is " + datetime.date.today().strftime("%B"))

#Delta time
azi = datetime.datetime.today()
ieri = azi - datetime.timedelta(days=1, hours=1)
maine = azi + datetime.timedelta(days=1)
print(azi, ieri, maine)
