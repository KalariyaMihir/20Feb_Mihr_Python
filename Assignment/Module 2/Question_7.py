# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

print("--- This Program is to Find that given number is Even or Odd ---\n\n")

number = int(input("Enter Number : "))

if(number % 2 == 0 ):
    print(f"{number} is Even Number.")
else:
    print(f"{number} is Odd Number.")