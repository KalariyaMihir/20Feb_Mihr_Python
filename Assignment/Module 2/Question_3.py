# Write a Python program to get the Fibonacci series of given range.

print("\n--- This Program is to Find Fibonacci of Given Number ---\n\n")

number = int(input("Enter Number : "))

n1 = 0
n2 = 1

for ind in range(1,number+1):

    print(n1)
    n3 =  n1 + n2
    n1 = n2
    n2 = n3
