##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import numpy as np
from collections import Counter
import csv
file = open('data.csv', 'r')

col0=[]; col1=[]; col2=[]; col3=[]; col4=[]; 

for line in file:
    
    data = line.strip().split("\t")            
    col0.append(data[0]); 
    col1.append(float(data[1])); 
    col2.append(data[2]); 
    col3.append(data[3]); 
    col4.append(data[4])    

chars = []
vals = []
tuples = []

for i, val1 in enumerate(col4):
    tuples1 = val1.split(",")
    for j, val2 in enumerate(tuples1):
        tuples2 = val2.split(":")
        #print(tuples2)
        tuples.append(tuples2)
        chars.append(tuples2[0])
        vals.append(tuples2[1])
        
uniquechars = sorted(Counter(chars).most_common())
for key in uniquechars:
    print(key[0],key[1], sep=",")
