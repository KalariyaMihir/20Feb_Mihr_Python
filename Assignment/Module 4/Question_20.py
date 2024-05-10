# Write python program that user to enter only odd numbers, else will raise an exception.

print("\n--- Program for only take odd number as an input else shoes exception ---\n\n")

number = int(input("Enter a Value : "))

try:
    if number%2==0:
        print("Number is Even : ")
        
except:
    print("Enter Only Odd Numbers ")