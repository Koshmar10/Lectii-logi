#avem de citit 5 inregistrari despre elevi
# (nume_elev punctaj_elev)
#1. convertor de note puctaj < 40 = F
#2. nota maxima
#3. nota minima
#4. frecventa notelor adica de cate ori apare fiecare nota  

def calificativ(puncte):
    #puncte (1-10)
    #sabilim intervalele
    # I S B FB 
    # I (1-4) S(5-7) B(8-9) FB(10)
    if puncte >=1 and puncte <=4:
        return 'I'
    elif puncte >= 5 and puncte <=7:
        return 'S'
    elif puncte >= 8 and puncte <=9:
        return 'B'
    else:
        return 'FB'
#faceti o functie care afiseaza fiecare elev si calificativul sau fiecare perechhe pe un rand nou
def afisare_calificative(catalog):
    #voi faceti
    for i in range(len(catalog)):
        inregistrare = catalog[i]
        print(inregistrare[0] + ' ' + calificativ(inregistrare[1]))

#nota maxima nota minima
#10 MINUTES!!!!!!!!!!!!!!!!!!!!!!
def nota_minima(catalog):
    #ori nota minima ori nota minima si elevul care o are
    minim = catalog[0]
    for i in range(len(catalog)):
        inregistrare = catalog[i]
        if minim[1] > inregistrare[1]:
            minim = inregistrare
    return minim
    pass
def nota_maxima(catalog):
    #//--//
    pass

catalog = []
'''
for i in range(5):
    inregistrare = input("Introdu numele si nota elevului\n")
    
    tmp = inregistrare.split(' ')
    tmp[1] = int(tmp[1])
    
    inregistrare= tuple(tmp)
    catalog.append(inregistrare)
'''
#afisare_calificative(catalog)
#print(nota_minima(catalog))

tuple1 = (10, 2, 9, 14, 2)
tuple2 = (10, 9, 2, 14, 2)
'''
# in
identic = True
for i in range(len(tuple1)):
    elem = tuple1[i]
    if elem not in tuple2:
        identic = False
if identic:
    print("sunt identice")
else:
    print("sunt diferite")
'''

identic = True
for i in range(len(tuple1)):
    elem = tuple1[i]
    count_elem = tuple1.count(elem)
    if count_elem != tuple2.count(elem):
        identic = False
if identic:
    print("sunt identice")
else:
    print("sunt diferite")
