# Write a Python program to find the length of a tuple.

print("This Program is for Find the Length of Given Tuple ---\n\n")

list = []

value = int(input("Enter Number of Entries : "))

for i in range(value):
    list.append(input("Enter Values : "))
    
tup = tuple(list)
print(f"Your Tuple : {tup}")
print(f"Length of Your Tuple is : {len(tup)}")

