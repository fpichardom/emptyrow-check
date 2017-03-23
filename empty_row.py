#!python3
import csv

file1 = input('File 1 Name: ')
n = input('Number of empty fields allowed:\n')
n = int(n)
delimiter = input('File delimiter: ')
with open(file1+'.csv','r') as file_1,\
    open('empty.csv','w', newline = '') as empty,\
    open('goodrecords.csv','w', newline = '') as good:
    reader = csv.reader(file_1, delimiter = delimiter)
    list1 = list(reader)
    header = list1[0]
    EmptyWriter = csv.writer(empty)
    GoodWriter = csv.writer(good)
    EmptyWriter.writerow(header)
    
    for i in list1[1:]:
        if i.count('') > n:
            EmptyWriter.writerow(i)
            list1.remove(i)
    for i in list1:
        GoodWriter.writerow(i)
        
        
            
        
