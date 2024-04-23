# Write a Python program to calculate the area of a parallelogram

print("\n--- This Program is to find the area of parallelogram ---\n\n")

def parallelogram(b,h):
    
    area = b*h
    
    print(f"Area of Your Parallelogram is : {area}")

base = int(input("Enter Value of Parallelogram : "))
height = int(input("Enter Height of Parallelogram :  "))

parallelogram(b = base,h = height)