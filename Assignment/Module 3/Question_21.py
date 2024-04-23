# Write a Python program to convert a tuple to a string.

print("\n--- This Program is for Convert a Tuple into String ---\n\n")

tuple = ('Dog', 'Cat', 'Mouse')
string = ''
for i in tuple:
    string += str(i)
    
print(string)