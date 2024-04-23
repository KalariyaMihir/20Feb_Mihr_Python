# parameterized polymorphism

class Arithmetic:

    def add(self,a,b):
        
        sum = a + b
        
        print(f"Sum of {a} and {b} : {sum}")
    
    def sub(self,a,b):
        
        sub = a - b
        
        print(f"Subtraction of {a} and {b} : {sub}")
    
    
    def mul(self,a,b):
        
        mul = a * b
        
        print(f"Multiplication of {a} and {b} : {mul}")
    
    
class Addition(Arithmetic):

    def add(self,a,b):
        return super().add(a,b)
    

class Subtraction(Arithmetic):

    def sub(self,a,b):
        return super().sub(a,b)


class Multiplication(Arithmetic):

    def mul(self, a, b):
        return super().mul(a, b)
    
    
ad = Addition()
sb = Subtraction()
ml = Multiplication()

print(ad.add(1,50))
print(sb.sub(45,12))
print(ml.mul(5,6))

    