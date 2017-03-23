#!python3
import csv

file1 = input('File 1 Name: ')
delimiter = input('File delimiter: ')
with open(file1+'.csv','r') as file_1,\
    open('selection.csv','w', newline = '') as empty:
    reader = csv.reader(file_1, delimiter = delimiter)
    list1 = list(reader)
    header = list1[0]
    EmptyWriter = csv.writer(empty)
    EmptyWriter.writerow(header)

    for i in list1[1:]:
        if i[1]=="." and i[2]==".":
            EmptyWriter.writerow(i)
        
            
        
