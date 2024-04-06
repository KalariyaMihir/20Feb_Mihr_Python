# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

print("\n--- This Program is to Print an Square of First & Last 5 Numbers of list ---\n\n")

list = []
new_list = []

for num in range(1,31):
    
    list.append(num)
    
for i in list[0:5]:
    new_list.append(i ** 2)


for i in list[-5:]:
    new_list.append(i ** 2)


print(f"Your List : {list}\n")
print(f"Square of First & Last 5 Elements of List is  :  {new_list}")

    
    
    
