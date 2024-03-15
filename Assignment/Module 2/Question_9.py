#  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

print("\n--- This Program is to print sum of three numbers and if two values are same answer will be Zero ---\n\n")

value_1 = int(input("Enter First Value : "))
value_2 = int(input("Enter Second Value : "))
value_3 = int(input("Enter Third Value : "))

sum = 0

if(value_1 == value_2 or value_2 == value_3 or value_1 == value_3):
    print(f"\nTwo Values are same and Answer is : {sum}")

else:
    sum = value_1 + value_2 + value_3

    print("ANSWER :- ")
    print(f"{value_1} + {value_2} + {value_3} = {sum} ")