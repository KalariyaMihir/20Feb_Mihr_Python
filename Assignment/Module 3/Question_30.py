# Write a Python program to convert a list of tuples into a dictionary.

print("\n--- This Program is to Convert list of tuple into a dictionary ---\n\n")

school = [(1,'Mihir',True), (2,'Hitesh',True), (3,'Abhisek',False)]

dict = {}

ind = 0
for i in range(1,len(school)+1):
    
    dict[i] = school[ind]
    print("\n")
    ind += 1
    
print(dict)

