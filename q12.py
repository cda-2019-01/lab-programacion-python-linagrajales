##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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
    
chars=[]
for val1 in col3:
    tuples1 = val1.split(",")
    chars+= tuples1
charsunique = sorted(list(set(chars)))

for chars0 in charsunique:
    count=0
    for i, val1 in enumerate(col3):
        tuples = val1.split(",")
        for chars in tuples:
            if(chars == chars0):
                count += int(col1[i])
    print(chars0+","+str(count))
