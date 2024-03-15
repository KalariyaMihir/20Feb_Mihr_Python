#  Write a Python program to get the Factorial number of given number.

print("\n--- This Program is to find Factorial of given number ---\n\n")

number = int(input("Enter Number : "))

fact = 1

for ind in range(1,number+1):
    fact *= ind

print(f"Factorial of {number} is : {fact}")