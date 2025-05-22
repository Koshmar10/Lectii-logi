import pandas as pd
import numpy as np
#pandas e un modul pentru prelucrare usoara a anumitor tipuri de fisiere
#data cleaning

#stergem coloanele pe care nu le dorim
#reindexam datele
#curatam coloanele 
#redenumim coloanele 
#sarim radnuri care nu ne trebuie

def read_data(file_path):
    #citire 
    #inchidere
    pd.set_option("display.max_columns", None) # nu am limita la numarul de coloane afisate
    pd.options.display.max_columns = None
    
    pd.set_option("display.max_rows", None) # nu am limita la numarul de randuri afisate
    pd.options.display.max_rows = None
    
    #prelucrare
    content = pd.read_csv(file_path)
    content = content.drop(columns=["Corporate Contributors", "Contributors", "Former owner", "Engraver", "Issuance type"])
    content = content.set_index("Identifier")
    print(content.head(7))

def row_data(index):
    content = pd.read_csv("lectii/library.csv")
    print(content["Identifier"].is_unique)
    content = content.set_index("Identifier")
    print(content.loc[index])

def clean_date():
    content = pd.read_csv("lectii/library.csv")
    content = content.set_index("Identifier")
    print(content.loc[1982:, "Date of Publication"].head(20))
    extraction = content['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    content['Date of Publication'] = pd.to_numeric(extraction)
    print()
    print(content.loc[1982:, "Date of Publication"].head(20))

def clean_place():
    content = pd.read_csv("lectii/library.csv")
    content = content.set_index("Identifier")
    print(content['Place of Publication'].head(10))
    london = content['Place of Publication'].str.contains('London')
    oxford = content['Place of Publication'].str.contains('Oxford')
    content['Place of Publication'] = np.where(oxford, 'Oxford', np.where(london, 'London', content["Place of Publication"]))
    print(content["Place of Publication"].head(10))
#read_data("lectii/library.csv")
#row_data(206)
#clean_date()
clean_place()
