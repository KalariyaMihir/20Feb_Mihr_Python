# Write a Python function that takes a list and returns a new list with unique elements of the first list.

print("\n--- This Program is to return the unique value from the list ---\n\n")


def unique():
    
    numbers = []
    uniq = []
    value = int(input("Enter how many Entries You want to do : "))

    for i in range(1,value+1):
        numbers.append(int(input(f"Enter {i} Value : ")))

    for i in numbers:
        
        if i not in uniq:
            uniq.append(i)
            
    print(f"Original List : {numbers}")
    print(f"Unique List : {uniq.sort()}")

unique()
            
  