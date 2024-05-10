# Write a Python program to count the number of lines in a text file.

import os

print("\n--- Write a Python Program to find number of lines in file ---\n\n ")

os.chdir('Assignment/Module 4')

file = open('lines.txt')

lines = len(file.readlines())

print(f"There is {lines} in Your File.")
