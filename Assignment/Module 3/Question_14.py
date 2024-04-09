# Write a Python program to find the second smallest number in a list.

print("\n--- This Program is to find the second Smallest number from List ---\n\n")

list = []
value = int(input("Enter Number of Entries : "))

for i in range(1,value+1):
     
     list.append(int(input(f"Enter {i} value : ")))
     
print(list)
ind1 = None
for i in list:
    
    if(i < ind1):
        ind1 == i

print(ind1)
        