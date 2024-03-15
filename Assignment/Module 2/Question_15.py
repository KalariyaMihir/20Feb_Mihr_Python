#  Write a Python program to count occurrences of a substring in a string.

print("\n--- This Program is to find Occurrence of a substring in a string ---\n\n")

string = input("Enter a Sentence : ")

find = input("Enter Substring(Word) : ")

occurrence = string.count(find)

print(f"Occurrence of '{find}' in ({string}) come's : {occurrence} Times.")