#Fisiere CSV
# C - Comma
# s - Separated
# v - Values
import csv
import random
#import pandas as p #modul pentru prelucrarea tuturor tipurilor de fisiere 

def read_csv(file_path):
    #primul pas deschidere fisier
    file = open(file_path, "r")
    #al doile citire
    content = file.readlines()
    csv_content = []
    for line in content[1:-1]:
        inregistrare = line.strip().split(', ')
        inregistrare = (
            int(inregistrare[0]),
            int(inregistrare[1]),
            int(inregistrare[2]),
            inregistrare[3].strip('"'),
            inregistrare[4].strip('"')

        )
        csv_content.append(inregistrare)
    
    #al treilea pas inchidem fisierul
    file.close()
    return csv_content

def print_row(row_number):
    csv_content=read_csv("lectii/oscar_age_female.csv")
    print(csv_content[row_number-1])

def oldest_female():
    csv_content = read_csv("lectii/oscar_age_female.csv")
    #presupun ca prima inregistrare contine cea mai in varsta femeie
    inregistrare_max = csv_content[0]
    #incep sa parcurg lista
    for inregistrare in csv_content:
    #pentru fiecare inregistrare compar varsta cu cea a inregistrarii pe care o consider maxima
        varsta_max = inregistrare_max[2] # varsta pe care o consider maxima
        varsta = inregistrare[2]
        if varsta > varsta_max:
            inregistrare_max = inregistrare
    #schimb inregistrarea maxima daca este nevoie
    print(inregistrare_max)

def secret_santa_shuffle(file_path):
    file = open(file_path, 'r')
    content = csv.reader(file, skipinitialspace=True)
    elevi = []
    for row in content:
        elevi.append(row[0])
    #(elev1, elev2) elev1 si elev2 isi dau cadouri unu altuia
    print(elevi)
    secret_santa = []
    elevi = elevi[1:]
    while elevi:
        index = random.randrange(0, len(elevi)) # o pozitie a unui nume random din lista 
        elev1 = elevi[index]
        elevi.pop(index)

        index = random.randrange(0, len(elevi))
        elev2 = elevi[index]
        elevi.pop(index)
        secret_santa.append((elev1, elev2))
    print(secret_santa)


print_row(2)
oldest_female()
secret_santa_shuffle("lectii/secret_santa.csv")