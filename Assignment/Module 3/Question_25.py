# Write a Python program to reverse a tuple.

print("\n--- this Program is to Reverse an given Tuple ---\n\n")


list = []

value = int(input("Enter Number of Entries : "))

for i in range(value):
    list.append(input("enter Values : "))
    
print(f"\nTuple : {tuple(list)} ")
list.reverse()
tup = tuple(list)


print(f"Reversed Tuple : {tup}") 