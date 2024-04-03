# Write a Python function to get the largest number, smallest num and sum of all from a list.

print("\n--- This Program is to find Largest, Smallest and Sum of all Numbers from List. ---\n\n")

def Calculation():
    
    numbers = []
    
    values = int(input("Enter How Many values you Want to Enter : "))
    
    for i in range(values):
        
        numbers.append(int(input("Enter Value : ")))
        
    # Code for finding Largest Number
    largest = numbers[0]
    for i in numbers:

        if(largest < i):

            largest = i

    print(f"\nLargest Number in Your List is : {largest}\n")
    
    
    # Code for finding lowest Number
    smallest = numbers[0]
    for i in numbers:
        if(smallest > i):
            smallest = i
    
    print(f"Smallest Number in Your List is : {smallest}\n")
    
    # Code for sum of all numbers
    sum = 0
    for i in numbers:
        sum += i
    print(f"Sum of all Numbers of Last is : {sum}\n")
    
Calculation()