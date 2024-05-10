# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

print("\n--- How to Define a Class in Python? What Is Self? Give An Example Of A Python Class ---\n\n")

print(""" 
      - We can Define Class using Class Keyword in 
      - Self is a first parameter of the any class method.
      - it allows us to access variables,attributes,and methods of a class.
      - Self is not an keyword so we can also use any other word.  
            
                                    -------------------------------------------------------------
                                    
      """)

class Student:
 
    def std(self):
        return(f"Student Name : {self.name}\nCorse Name : {self.course}\nCourse Fee : {self.fees}")
        
st1 = Student()

st1.name = 'Mihir Kalariya'
st1.course = 'PYTHON'
st1.fees = 40000


print(st1.std())
