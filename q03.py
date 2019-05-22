##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import numpy as np
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
    
    col0join = "".join(col0)
charcounts = sorted(Counter(col0join).most_common())
    
for i in range(0,len(charcounts)):    
    
    sum = 0
    for j, val in enumerate(col0):
        if(charcounts[i][0]==val):
            sum+=col1[j]
    print(charcounts[i][0]+","+str(int(sum))) 
