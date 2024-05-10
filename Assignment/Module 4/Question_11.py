# Write a Python program to write a list to a file.

print("\n--- This Program is to write list into file ---\n\n")

import os

value = int(input("Enter How many Values you want to Enter :  "))
items = []
for i in range(value):
    
    items.append(input("Enter an Value : "))

os.chdir('Assignment/Module 4')

file = open('lists.txt','w')

for j in items:
    # print(j)
    file.write(j)
    file.write('\n')
    

file.close



