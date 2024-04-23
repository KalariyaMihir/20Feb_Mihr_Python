# user input in class

class Sum:
    
    n1 = int(input("Enter First Value : "))
    n2 = int(input("Enter Second Value : "))
    sum = 0

    def add(self):
        
        self.sum = self.n1 + self.n2

        
    def show(self):
        print(f"Addition of {self.n1} + {self.n2} = {self.sum}")
         
addition = Sum()

addition.add()
addition.show()
