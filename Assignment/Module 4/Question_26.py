# What is Instantiation in terms of OOP terminology?

print("\n--- What is Instantiation in terms of OOP terminology? ---\n\n")

print("""
      - Instantiation in oop terminology is Creating an object of an class.
      - Class is just a blue print or design until we create an instance (object).
      - instance is used to call members, methods or constructor.   
    """)

class Employee:
    
    def emp(self,id,name,salary):

        print("Id :",id)
        print("Name :",name)
        print("Salary :",salary)


# here emp1 is an instance of an Employee 
emp1 = Employee()

emp1.emp(101,'Mihir Kalariya',50000)