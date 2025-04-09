#Lectia 5
#Matrici
#liste [12, 'salut', 34, True]
#matrice [[], [], [], []]
#matricea este o lista de liste
#
#   0 1   
#0  6 7  
#1  9 5 
#
#  7 9 5 
#  0 1 2 
#
# 1 2 3 4 -linie
# 1 2 8 9 - coloana
matrice = [[1, 2, 3, 4], [2, 3, 10, 12], [8, 7, 3, 2], [9, 21, 3, 1]]
import random
#Task 1
#print(matrice)
def printMatrice(m):
    for line in m:
        for element in line:
           print(element, end = " ")
        print("")
#O matrice este formata din linii si coloane
#Task 2
def generareMatrice(linii , coloane): #linii = n coloane = m
    matrice = []
    for i in range(linii):
        linie = []
        for j in range(coloane):
            linie.append(random.randrange(1, 11))
        matrice.append(linie)
    return matrice

def definireMatrice():
    linii=int(input("Introdu numarul de linii: "))
    coloane=int(input("Introdu numarul de coloane: "))
    numar_elemente = linii * coloane
    #varianta 1 lista auxiliara
    '''
    lista_aux=[]
    while numar_elemente > 0:
        numar = input()
        if numar.isalnum() and numar != '':
            numar = int(numar)
            lista_aux.append(numar)
            numar_elemente-=1
    '''
    elemnte_matrice = input("introdu elementele: ")
    elemnte_matrice = elemnte_matrice.split()

    matrice = []
    for i in range(linii):
        linie = []
        for j in range(coloane):
            linie.append(int(elemnte_matrice[0]))
            elemnte_matrice.pop(0)    
        matrice.append(linie)
    return matrice
#  0  1
#0 10 5
#1 5 6
#
#
#
def sumaMatrice(matrice):
    suma = 0
    for i in range(len(matrice)): # i = indexul liniei
        for j in range(len(matrice[i])): # j = indexul coloanei// elementului de pe linia cu indexul i 
            suma+=matrice[i][j] #elementul de pe linia i si coloana j
    print(suma)
    '''
    for linie in matrice:
        for element in linie:
            suma+=element
    '''


#matriceNou=generareMatrice(5, 5)
#printMatrice(matriceNou)

matriceaMea=definireMatrice()
printMatrice(matriceaMea)
#Se da o matrice si fiecare linie reprezinta notele unui elev 
#sa se faca media aritmetica pentru fiecare linie a matricei
# 4 6 
# 2 3 
# 
# mediile sunt 5.0 2.5