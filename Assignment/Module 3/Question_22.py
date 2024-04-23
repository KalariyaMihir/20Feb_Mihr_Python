# Write a Python program to check whether an element exists within a tuple.

print("\n--- This Program is to find whether given element exists in Tuple ---\n\n ")

tuple = ('Red', 'Green', 'Blue', 'Orange', 'Black', 'Purple', 'Yellow', 'White')

print("-- Enter Name of Color --")
value = input("Enter an Element to find it Existence : ")

if value in tuple:
    print(f"\n{value} Exists in Tuple")
    print(f"Your Tuple : {tuple}")

else:
    print(f"\n{value} Doesn't Exists.\n")
    print(f"Your Tuple : {tuple}")