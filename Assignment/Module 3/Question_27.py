# Write a Python program to find the repeated items of a tuple.

print("\n--- This Program is to find the repeated items of tuple ---\n\n")


list = ['M','I','H','I','R','M']

# value = int(input("Enter Number of Entries : "))

# for i in range(value):
    # list.append(input("enter Values : "))
    
tup = tuple(list)

 
# vl = input("Enter Value to count : ")
for i in tup:
    
    if (tup.count(i) >= 2):

        print(i)


        
        
        
        # incomplete code


    
