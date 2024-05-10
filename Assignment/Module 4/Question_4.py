# Write a Python program to read first n lines of a file.

print("\n--- This Program is to read n number of lines on user input ---\n\n")

import os

os.chdir('Assignment/Module 4/')

file= open('lines.txt','r')

line = int(input("How many lines you want to Read :"))

for i in range(1,line+1):
    
    print(file.readline())
    
file.close()

