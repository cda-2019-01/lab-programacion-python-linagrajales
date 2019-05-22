##
## Imprima la suma de la segunda columna.
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
np.asarray(col1).sum()
