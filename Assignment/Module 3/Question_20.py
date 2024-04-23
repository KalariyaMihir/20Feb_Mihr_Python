# Write a Python program to create a tuple with numbers.

print("\n--- This Program is for Create an Tuple with Numbers ---\n\n")

values = int(input("Enter the numbers of Entries : "))

list = []

for i in range(values):
    
    list.append(int(input("Enter Value : ")))

tuple = tuple(list)

print(tuple)

