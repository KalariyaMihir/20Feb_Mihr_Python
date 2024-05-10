# Write a Python program to read a file line by line store it into a variable.

import os

print("\n--- This Program is to read file line by line and store it into a list ---\n\n")

os.chdir('Assignment/Module 4')

try:

    container = ''

    file = open('lines.txt','r') 

    for i in range(10):

        container += file.readline()

    print(container)
    
except:
    
    print("OOPS There is some error")
    