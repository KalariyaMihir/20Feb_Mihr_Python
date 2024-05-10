# Write a Python program to read an entire text file.
import os
print("\n--- Program to Read an Entire Text file. ---\n\n")

os.chdir("Assignment\Module 4\ ")

file = open('hello.txt','r')

print(file.read())

file.close()
