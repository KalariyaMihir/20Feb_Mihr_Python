# Write a Python program to append text to a file and display the text.
import os

print("\n--- This Program is for append text to the file and display ---\n\n")

os.chdir('Assignment\Module 4')

file_a = open('Details.txt','a')

line = input("Write Something here : ")

file_a.write(line)
file_a.close()

file_r = open('Details.txt','r')

read = file_r.read()

print(read)

file_r.close()