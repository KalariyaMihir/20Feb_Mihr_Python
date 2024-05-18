# What relationship is appropriate for Student and Person?

print("\n--- What relationship is appropriate for Student and Person? ---\n\n")

print("""
      
      - For Student and person Multilevel inheritance is appropriate.
      - e.g.
      """)

class Person :
    
    def person(self,pr_name):
        
        self.pr_name = pr_name

class Student(Person):        
        
    def Student(self,st_name,st_course):
        
        print("\n---------------------------------------------------------------")
        print(f"\nStudent Name is : {st_name}")
        print(f"Student Course is : {st_course}")
        print(f"{self.pr_name} is Reference of {st_name}\n")
        
st = Student()

stName = input("Enter Student Name : ")  
stCourse = input("Enter Student Course : ")
prName = input("Enter Reference Person Name : ")

st.person(prName)
st.Student(st_name = stName,st_course=stCourse)

