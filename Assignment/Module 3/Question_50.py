# Write a Python function to check whether a number is perfect or not.

print("\n--- This Program is to check the given number is proper number or not ---\n\n")

num = int(input("Enter an Number : "))

def perfect(value):
    
    sum = 0
    
    for i in range(1,value):
    
        if(value%i == 0):
            sum += i
            
    if (sum == value):
        print(f"{value} is Perfect Number.")
            
perfect(num)
