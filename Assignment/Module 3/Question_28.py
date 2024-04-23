# Write a Python program to remove an empty tuple(s) from a list of tuples.

print("\n--- This Program is Remove empty values from tuple ---\n\n")

tup = ('Mango', 'Banana','', 'Orange', 'Apple', 'Pineapple')

print(f"\nTuple with Empty Values : {tup}")

list = list(tup)

for i in list:
    
    if(i == ''):
        list.remove(i)
        
print(f"Tuple After Removing Empty Values : {tuple(list)}")

 