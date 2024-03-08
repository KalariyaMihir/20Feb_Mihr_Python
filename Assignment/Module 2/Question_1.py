# Write a Python program to check if a number is positive, negative or zero.

print("\n--- This Program is to Find that entered number is Positive negative or zero ---\n")
number = int(input("Enter an Number : "))

if(number > 0):
    print(f"{number} is positive number.\n")

elif(number < 0):
    print(f"{number} is negative number.\n")

else:
    print("You have entered 0(ZERO).\n")
