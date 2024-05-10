# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

print("\n--- This Program is to find the area and perimeter of a circle using class ---\n\n ")

class Circle:

    def __init__(self,radius,pie) :

        self.radius = radius
        self.pie = pie


    # method to find an area of circle 
    def circleArea(self):

        area = self.pie * self.radius*self.radius
        
        return(f"Area of Circle is : {area}")
    
    # method to find an perimeter of circle
    def circlePerimeter(self):
        
        perimeter = 2*self.pie*self.radius
        
        return(f"Perimeter of Circle is : {perimeter}")
    


radius = int(input("Enter Radius of Circle : "))

crcl = Circle(radius,3.14)



print("""
               What dO You want to Calculate :
               
                        Press 1 : To Find Circle 
                        Press 2 : To Find Perimeter
                        
            """)

choice = int(input("Enter Choice : "))        

# returns the area of circle
if (choice == 1):
    print(crcl.circleArea())

# returns perimeter of circle
 
elif(choice == 2):
    print(crcl.circlePerimeter())
    
else:
    print("OOPS! Wrong input .")
