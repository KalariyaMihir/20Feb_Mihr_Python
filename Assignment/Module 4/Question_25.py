# Explain Inheritance in Python with an example? What is init? Or Con?

print("\n--- Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? ---\n\n")

print("""
      - Constructor is a block of code the initialize newly created object.
      - Constructor is a method that is called automatically when we create the object of an class.
      - Generally constructor has the same name as the class name.
      - In Python Constructor is define with __init__ 
      - __init__ is a constructor in python and it doesn't have.  
      
      
      Example :
      
      """)

class OPERANDS:
    a :int
    b: int
    def __init__(self) :
        self.a = int(input("Enter First Value : "))
        self.b = int(input("Enter Second Value : "))
        
        
class Sum(OPERANDS):
    
    def __init__(self):
        
        super().__init__()
        
        c = self.a + self.b
        
        print(f"Sum of {self.a} and {self.b} is : {c}")

add = Sum() 

  