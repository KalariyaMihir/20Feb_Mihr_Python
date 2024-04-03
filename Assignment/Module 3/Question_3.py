# Differentiate between append () and extend () methods?

print("\n--- This Program is to show Difference Between Append and extend method ---\n\n")

print("""Append : 
        
        - Append method is used to add new element. 
        - it add's element in the end.
        
        - Example : \n""")

list1 = [1,2,3,4]

print(f"list Before Append : {list1}")

list1.append(input("Enter Value : "))        
print(f"List After Append : {list1}")

print("\n--------------------------------------------------------------------------\n")

print("""Extend : 
      
        - Extend method is used to concat two lists.

        - Example : \n""")


l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

print(f"First List : {l1}")
print(f"Second List : {l2}")

l1.extend(l2)

print(f"Extended List is : {l1}")



