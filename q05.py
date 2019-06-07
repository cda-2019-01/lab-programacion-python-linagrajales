##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
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
from collections import Counter
col0join = "".join(col0)
charcounts = sorted(Counter(col0join).most_common())
    
for i in range(0,len(charcounts)):    
    
    max = 0
    min = 6
    for j, val in enumerate(col0):
        if(charcounts[i][0]==val):
            if col1[j]>max:
                max=col1[j]
            if col1[j]<=min:
                min=col1[j]
    print(charcounts[i][0]+","+str(int(max))+","+str(int(min))) 
