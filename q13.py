##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
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
    
tuples = []

for i, val1 in enumerate(col4):
    tuples1 = val1.split(",")
    x = np.array([])
    for j, val2 in enumerate(tuples1):
        tuples2 = val2.split(":")
        tuples.append(tuples2)
        x = np.append(x,[float(tuples2[1])],axis=0)
    print(str(col0[i])+","+str(int(x.sum())))
