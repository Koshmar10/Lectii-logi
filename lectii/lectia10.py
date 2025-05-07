#Tuple
#lista este mutable
# adica se poate modifica, extinde sterge
'''
numere = [10 ,20, 5, 3]
print(numere)
numere.append(25)
print(numere)
numere.remove(20)
print(numere)
numere[0] = 30
#fun fact sterge elementul din lista
del numere[2]

print(numere)
# tuple este imutable
myTuple=(20, 30, 20, 10)
#nu am voie sa o extind
#myTuple.append(5)
myTuple[0] = 70
print(myTuple)
#unde ma ajuta
elev = ('Petru', 'cnp=50324232')
cnpNou = 'cnp=1232121'
#elev[1] = cnpNou 
'''
#o tupla nu poate fi extinsa nici micsorata
# tuple - imutable 
# list - mutable
#task 3 Conversie
tuple1 = ('Mihai', 'Andrei')
print(tuple1)
tuple1 = list(tuple1)
tuple1[1] = 'Clara'
tuple1 = tuple(tuple1)
print(tuple1)
#tuple -> list -> modificari  -> tuple
#slicing
#Task 4
longTuple = (3, 4, 10, 2, 1, 9)
print(longTuple[1:4])
print(longTuple[-4:-1])
##invsrare
print(longTuple[::-1])

#comparare de tuple
a = (1, 2, 3)
b = (1, 2, 3)
if a == b:
    print('a == b')

print(len(a))

#Task 5
import random
elemente = 5
#metoda 1 
'''
list1= []
for i in range(elemente):
    list1.append(random.randint(1, 10))
'''
#metoda 2 - comprehensiune
list1= [ random.randint(1,10) for x in range(elemente)]
tuple1= tuple(random.randint(1,10) for x in range(elemente))
x = 5
if x in tuple1:
    print('x in tuple1')
print(list1, tuple1)
# tuple = (nume, varsta)
persoana1 = ('Mihai', 17)
persoana2 = ('Andrei', 14)
persoana3 = ('Clara', 14)
persoana4 = ('Stefan', 15)
#lista cu toate persoanele
persoane = list((persoana1, persoana2, persoana3, persoana4))
print(persoane)
#numaram cate persoane au varsta para
#parcurgere = merg prin lista element cu element
contor = 0
for persoana in persoane:
    if persoana[1] % 2 == 0:
        contor += 1
print(contor)
# numarati persoanele cate au litera a in nume
# x = a nume= Alex --- if x in nume:  # verific daca variabila x e in nume
contor = 0
for persoana in persoane:
    if 'a' in persoana[0]:
        contor+=1
print(contor)
#pasu1 1 
# persoana = (Mihai, 17)
# 'a' in persoana[0]
#pasul 2 
# persoana = (Andrei, 14)
#'a' in persoana[0]
#pasul 3
#persoana = (Clara. 14)
# 'a' in persoana[0]


#concatenare muliplicare
a = (1, 2, 3)
b = (7, 5, 6)
print( a + b)
print( 3 * a) # a + a + a