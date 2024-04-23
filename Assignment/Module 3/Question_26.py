# Write a Python program to replace last value of tuples in a list.

print("\n--- This Program is to Replace the last value of tuple in list ---\n\n")

tpl = ('One', 'Two', 'Three', 'Four', 'Six')

print(tpl,'\n')
values = input("Enter Value to Replace the last Index : ") 

list = list(tpl)

list.insert(-1,values)

tup = tuple(list)

print(tup)