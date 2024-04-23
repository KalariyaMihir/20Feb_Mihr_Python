# Write a Python program to convert a list to a tuple.

print("\n--- This Program is to Convert List into Tuple ---\n\n")

list= []

value = int(input("Enter Number of Entries : "))

for i in range(value):
    list.append(input("Enter Value : "))

print(f"\nYour List : {list}")

tup = tuple(list) 

print(f"\nTuple after Type Casting : {tup}")