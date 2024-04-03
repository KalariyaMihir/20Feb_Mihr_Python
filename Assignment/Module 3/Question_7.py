# Write a Python program to remove duplicates from a list.

print("\n--- This Program is for Remove Duplicate Values form an List. ---\n\n")


value = int(input("Enter How many values you want to Enter : "))

listt = []

for i in range(value):

    listt.append(input("Enter an String : "))

temp = set(listt)


print(list(temp))



