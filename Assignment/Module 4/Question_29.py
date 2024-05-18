# What relationship is appropriate for Course and Faculty?

print("\n--- What relationship is appropriate for Course and Faculty? ---\n\n")

print("""
      
      - Course Faculty share the Multiple Inheritance. 
      - e.g.
      
      """)


# class Course :
    
#     course : str
    
#     def __init__(self):

#         self.course  = input("Enter Course Name : ")


# class Faculty(Course):
    
#     FacultyName : str
#     FacultySubject : str

    
#     def __init__(self):
        
#         # calling the parent class's Constructor(method) using super
    
#         FacultyName = input("Enter Faculty Name : ")
#         FacultySubject = input("Enter Faculty Subject : ")

#         super().__init__()
#         print(f"""
#               - Faculty Name : {FacultyName}
#               - Faculty Subjects : {FacultySubject}
#               - Course Name : {self.course}
#               """)
   
         
# fc = Faculty()



class Course1:
    
    def course1(self):
        self.course_1 = 'Python'

class Course2:
    
    def course2(self):
        self.course_2 = 'IOS'
        
class Course3:
    
    def course3(self):
        self.course_3 = 'Digital Marketing'

class Faculty(Course1,Course2,Course3):
        
    def __init__(self,name):
        
        super().course1
        super().course2
        super().course3

        print(f"Faculty Name : {name}")

        print(f"{name} Teach's : {self.course_1},{self.course_2},{self.course_3}")

faculty_name = input("Enter Name of Faculty : ")

fc = Faculty(faculty_name)
