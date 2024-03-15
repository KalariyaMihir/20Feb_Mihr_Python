#  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

print("\n--- This Program returns true if the two given integer are equal or their sum or difference is 5 ---\n\n")

value_1 = int(input("Enter First Value : "))
value_2 = int(input("Enter Second Value : "))


if(value_1 == value_2 or value_1 + value_2 == 5 or value_1 - value_2 == 5):
    print(True)

else:
    print(False)
