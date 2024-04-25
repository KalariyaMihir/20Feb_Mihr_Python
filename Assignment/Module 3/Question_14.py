# Write a Python program to find the second smallest number in a list.

print("\n--- This Program is to find the second Smallest number from List ---\n\n")

list = []
value = int(input("Enter Number of Entries : "))

for i in range(1,value+1):
     
     list.append(int(input(f"Enter {i} value : ")))
     
     
print(f"Your List : {list}")
sorted(list)

print(f"Second Smallest Number is : {list[1]}")