# student info polymorphism

class InfoDetails:
    
    def info(self,id,name,subject):
        
        print(f"Student Id : {id}")
        print(f"Student Name : {name}")
        print(f"Student Subject : {subject}")


class Std1(InfoDetails):
    def info(self, id, name, subject):
        return super().info(id, name, subject)
    
class Std2(InfoDetails):
    def info(self, id, name, subject):
        return super().info(id, name, subject)

class Std3(InfoDetails):
    def info(self, id, name, subject):
        return super().info(id, name, subject)

s1 = Std1()
s2 = Std2()
s3 = Std3()
        
print(s1.info(101,'Mihir','Full Stack Python'))
print(s2.info(102,'Hitesh','Full Stack'))
print(s3.info(103,'Abhishek','Java'))
