# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

print("\n--- This Program is to find the area of rectangle with the help of class ---\n\n")

class Rectangle:
    
    # constructor
    def __init__(self,length,width) :
        
        self.length = length
        self.width = width
    
    # method to calculate are of rectangle  
    def area(self):
        
        area = self.length * self.width 
        
        return(f"\nArea of Rectangle is : {area}")
    
    
length = int(input("Enter Length of Rectangle : "))
width = int(input("Enter width of Rectangle : "))

    
rect = Rectangle(length,width)

print(rect.area())
