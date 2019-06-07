##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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

for i, vals1 in enumerate(uniquechars):
    x = np.array([])
    for j, vals2 in  enumerate(tuples):
        if(vals1[0]==vals2[0]):
            #print(vals2[1])
            x = np.append(x,[float(vals2[1])],axis=0)
    print(vals1[0]+","+str(int(x.min()))+","+str(int(x.max())))
