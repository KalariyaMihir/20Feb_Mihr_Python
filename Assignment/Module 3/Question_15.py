# Write a Python program to get unique values from a list


list = []

entries = int(input("Enter Numbers of Entries : "))

for n in range(entries):
    list.append(input("Enter Value : "))
    
print(list)

for i in list:
    
    if (type(i) == str):
        pass
    else:
        print(i)
    