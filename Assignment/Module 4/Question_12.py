# Write a Python program to copy the contents of a file to another file.

import os

print("\n--- This Program is to copy content from one to another ---\n\n")

os.chdir('Assignment/Module 4')


file1 = open('paragraph.txt','r')

data = file1.read()

file2 = open('New_file.txt','w')

file2.write(data)

file2.close()
file1.close()

