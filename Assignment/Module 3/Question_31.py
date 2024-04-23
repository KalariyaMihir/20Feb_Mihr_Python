# How will you create a dictionary using tuples in python? 

print("\n--- This Program creates dictionary from tuples ---\n\n")

values = int(input("Enter Values for Tuple : "))

l1 = []
l2 = [] 

for i in range(1,values+1):
    l1.append(input(f"Enter {i} key: ")) 
    l2.append(input(f"Enter {i} Value : ")) 

tpl1 = tuple(l1)
tpl2 = tuple(l2)

dict = {}

for i in range(values):
    
    dict[l1[i]] = l2[i] 

print(dict)

