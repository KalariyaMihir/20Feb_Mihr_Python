#  Write a python program to sum of the first n positive integers.

print("\n --- This Program give sum of integer numbers on users input ---\n\n")

value = int(input("enter Number : "))

sum = 0

for ind in range(1,value+1):

    sum += ind 

print(f"Sum of {value} Positive number is : {sum}")