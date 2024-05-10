# What is File function in python? What is keywords to create and write file.
import os

print("\n--- What File Function and Keyword to create an write an File ---\n\n")

print('''
      
      - File Function used to create read or write data in file or from file
      - we can store data in files  
      - to create an file we 
      
      
      ''')

os.chdir('Assignment\Module 4')

file = open('hello.txt','w')

file.write("Hello World")

file.close()