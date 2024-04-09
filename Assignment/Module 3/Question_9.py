# Write a Python function that takes two lists and returns true if they have at least one common member.

print("\n--- This Program is return true if two lists has the same values ---\n\n")

list1 = []
list2 = []

value = int(input("Enter Value of Entry for First List : "))

print("-> First List : \n")

for i in range(value):
    list1.append(input(f"Enter {i} Value : "))
    
print("-> Second List : \n")
for i in range(value):
    list2.append(input(f"Enter {i} Value : "))
     
print(list1,list2,"\n")

for item in list1:
    
    if item in list2:  
        print(True)
        
    


