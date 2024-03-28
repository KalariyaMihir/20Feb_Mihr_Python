# UDF for find area

def circle(r):
    area = 3.14 * r * r
    
    print("Area of Circle is : ",area)

def rectangle(width,length):
    
    area = length * width
    
    print("Area of Rectangle is : ",area)
    
def square(size):
    
    area = size * size
    print ("Area of Square is : ",area)
    



print("Press 1 : Find Area of Circle")
print("Press 2 : Find Area of Rectangle")
print("Press 3 : Find Area of Square")

choice = int(input("Enter a Choice : "))


if(choice == 1):
    
    radius = int(input("Enter Radius if Circle : ")) 
    circle(radius)
    
elif(choice == 2):
    
    width = int(input("Enter Width of Rectangle : "))
    height = int(input("Enter Width of height : "))

    rectangle(width , height)
    
elif(choice == 3):
    
    size = int(input("Enter Size of Circle : "))

    square(size)
    
else:
    print("Invalid Choice")