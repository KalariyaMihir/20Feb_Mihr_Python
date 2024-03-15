# Write a Python program to count the number of characters (character frequency) in a string

print("\n--- This Program is to count the number of character's in string ---\n\n")

string = input("Enter a String : ")

find = input("Which Character : ")
count = string.count(find)

print(f"{find} in {string} come's : {count} times")