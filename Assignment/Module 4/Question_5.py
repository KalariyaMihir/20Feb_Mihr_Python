# Write a Python program to read first n lines of a file.

print("\n--- This Program is to read last n number of lines on user input ---\n\n")

import os

os.chdir('Assignment/Module 4/')

file= open('lines.txt','r')

lines = int(input("How many lines you want to Read :"))

read = file.readlines()

for i in read[-lines : ]:
    print(i)

file.close()

