# Write a Python program to count the frequency of words in a file.

import os

print("\n--- find the frequency of words in a file ---\n\\n" )

os.chdir('Assignment/Module 4')

file = open('paragraph.txt')
count = 1
word = input("Enter word to find it's Frequency : ")
if word in file.read():
    count+=1
    print(f"{word} is {count} times in File.")
    
else:
    print("There is no such word in File.")