import pandas as pd
import numpy as np

dataset1 = pd.read_csv('Books.csv', dtype={'Year-Of-Publication': str})
dataset2 = pd.read_csv('Ratings.csv')
dataset3 = pd.read_csv('Users.csv')

#C1

diccionario = {}

for ISBN in dataset2.ISBN.values:
    if ISBN not in diccionario:
        diccionario[ISBN] = 1
    else:
        diccionario[ISBN] += 1

c1_pre= max(diccionario, key=diccionario.get)
c1_count= max(diccionario.values())
print(c1_pre)
print(c1_count)
titulo = dataset1.loc[dataset1['ISBN'] == f"{c1_pre}", 'Book-Title'].values[0]
print(titulo)
