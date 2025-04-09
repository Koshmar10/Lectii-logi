#LECTIA 4
#Ce este o functie?
#O functie o secventa de cod care produce un rezultat 
#EX: def suma(a, b): return a+b
#Generatoare
#Exemplu
'''
def sir(capatSir):
    for i in range(1, capatSir):
        yield i
for elemnt in sir(6):
    print(elemnt, end=' ')
'''
#Faceti un generator care imi da un sir de numere pare pana la o
#anumita valoare
'''
def evenNumberGenerator(rangeLimit):
    for i in range(0, rangeLimit, 2):
        yield i
for i in evenNumberGenerator(11):
    print(i, end=" ")
'''
#Task 3-4-5-6
#Se da o lista de produse si o lista in care putem gasi preturile
#asociate fiecarui produs(produsul de pe pozitia i din lista 
#de produse are asociat pretul de pe pozitia i din lista de
#preturi)
#Avem nevoie de o functie care ne cere un numar de produse
#pe care sa le cumparam si ne alege atatea produse random din lista
#Vom scrie si o functie care calculeaza pretul total al produselor
#de cumpatat, o functie care ne spune cel mai scump produs,
#si o functie care ne spune cel mai ieftin produs

#in python avem instructiuni gen print(), a=20, 
#avem structuri repetitive gen for while (executa o bucata de cod de x ori)
#structuri de decizie gen if (in functie de o conditie se executa o anumita bucata de
#cod sau nu)
import modul
import random
listaDeProduse=['Banane', 'Paine', 'Cola', 'Pateu', 'Parizer']
listaDePreturi=[6.0, 10.50, 7.24, 1.50, 2.50]
listaDeCumparaturi=[]

def pozitieElement(lista, element):
    for i in range(len(lista)):
        if lista[i] == element:
            return i

def creazaListaDeCumparaturi(produse, preturi):

    numarDeProduse=int(input("Introdu un numar de produse de cumparat: "))
    for i in range(numarDeProduse):
        produsSelectat=listaDeProduse[random.randrange(0, len(listaDeProduse))]
        listaDeCumparaturi.append(produsSelectat)

def costTotal(listaDeCumparaturi):
    cost=0
    for produs in listaDeCumparaturi:
        pozitieProdusInLista=pozitieElement(listaDeProduse, produs)
        cost += listaDePreturi[pozitieProdusInLista]
    print(cost)


creazaListaDeCumparaturi(listaDePreturi, listaDeCumparaturi)
print(listaDeCumparaturi)
costTotal(listaDeCumparaturi)
#DE FACUT
#functie pentru cel mai scump produs din lista de cumparaturi
#functie pentru cel mai ieftin produs din lista de cumparaturi
