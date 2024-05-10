# Write a Python program to read a file line by line and store it into a list

import os

print("\n--- This Program is to read file line by line and store it into a list ---\n\n")

os.chdir('Assignment/Module 4')
try:
    file_list = [] 
    
    file = open('lines.txt','r') 
    for i in range(10):
        line = file.readline()
        file_list.append(line)

    print(file_list)
    
except:
    print("OOPS There is some error")
    