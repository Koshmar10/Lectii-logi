def mediaAritmetica(a, b):
    return (a+b)/2

def estePrim(x):
    if x == 2:
        return True
    if x%2 == 0:
        return False
    for d in range(3, x//2):
        if x%d == 0:
            return False
    return True


def afisareNumerePrime(n):
    for num in range(0, n):
        if estePrim(num) == True:
            print(num, end=" ")
    return
def generareMatrice(randuri, coloane):
    matrice = []
    for i in range(randuri):
        rand=[]
        for j in range(coloane):
            rand.append(0)
        matrice.append(rand)
    return matrice
#Scrieti o functie care genereaza o lista de n numere random
import random
def generareLista(n):
    #genereati lista cu numere random
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return list
print(generareLista(10))