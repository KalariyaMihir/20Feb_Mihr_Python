# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

print("\n--- This Program is to remove last object from the list ---\n\n")

list1 = [2,33,222,14,25]

print("-> To Remove an ALsat Object from List we can use pop() method it removes the LAST elements.")
print("-> -1 Index is negative indexing and it's starts from the end.\n")

print(f"List : {list1}")
print(f"Example : {list1[-1]}")

list1.pop()
print(f"List After Removing Last Element : {list1}")

