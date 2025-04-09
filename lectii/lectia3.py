#lectia 3 module
import math
import random
import matplotlib.pyplot as plt
import modul 
#Task 1
'''
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

#Task 2
def cerc(raza):
    print("Aria cercului este", round(math.pi * raza ** 2))
cerc(4)
print(math.factorial(5))
print(math.sqrt(4))
#Task 4
numbers = []
lungime_numbers=16
for i in range(lungime_numbers):
    numbers.append(random.randrange(1, 10, 1))
print(numbers)
#task 5
incercari=7
numar_de_ghicit=random.randint(1, 101)
numarul_meu=0
while numar_de_ghicit != numarul_meu and incercari > 0:
    numarul_meu = int(input("Da-mi un numar:"))
    if numar_de_ghicit > numarul_meu:
        print("Am nevoie de un numar mai mare")
    if numar_de_ghicit < numarul_meu:
        print("Am nevoie de un numar mai mic")
    incercari-=1
    if numar_de_ghicit == numarul_meu:
        print("Bravo ai castigat jocul s-a terminat")
        break
#Task 6
'''
modul.salut('petru')
print(modul.profesor)