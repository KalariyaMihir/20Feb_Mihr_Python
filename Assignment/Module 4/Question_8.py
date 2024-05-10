# Write a python program to find the longest words.

import os

print("\n--- Find Longest word from File ---\n\n")

os.chdir('Assignment/Module 4')

file = open('paragraph.txt','r')

maxLength = 0

word = ''
for i in file.read().split():

    if (len(i) >= maxLength):
        maxLength = len(i)
        word = i
    
print(f"{word} is the Longest Word in the file with Length of {maxLength} character.")


