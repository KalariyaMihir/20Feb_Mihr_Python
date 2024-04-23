# create a banking system using oops
import random

class UserDetails():

    name : str
    a_no :int
    balance : int 
    a_type : str 
    
    def details(self):
          
        self.name = input("Enter Your Name : ")
        self.a_no = random.randint(11111111111,99999999999)
        self.balance = float(input("Enter Your Bank Balance : "))
        self.a_type = input("Enter Your Account type S/C: ")
        
class Withdraw(UserDetails):
    
    amount : int
    
    def withdraw(self):
        print("--- You Are Withdrawing Money ---")
        self.amount = int(input("Enter Withdraw Amount : "))

        if(self.balance >= self.amount):
            self.balance -= self.amount
            print(f"{self.amount} has been debited from your {self.a_no}")
            print(f"{self.balance} has been Remaining")
        else:
            print("-- Inefficient Balance --")

class Deposit(Withdraw):
    
    amount : int 
    
    def deposit(self):
        print("-- You are Depositing Money --")
        
        self.amount = int(input("Enter Deposit Value : "))
        if (self.amount >= 2000):
            self.balance += self.amount
            print(f"{self.amount} has been credited to Your account {self.a_no}")
            print(f"Total Balance is {self.balance}")
            
        else:
            print("Minimum Balance should be 2000")
            
    
class Statement(Deposit):
    
    def statement(self):
        
        print(f"Account no : {self.a_no}")
        print(f"Account Holder Name : {self.name}")
        print(f"Account Type : {self.a_type}")
        print(f"Account Balance : {self.balance}")
        

bank = Statement()

print(bank.details())

print("""
      
                        ---------------------------------------------------------------------------------------------------

                            Withdraw : Press 1
                            Deposit : Press 2
                            Statement : Press 3""")

choice = int(input("Enter Your Choice : "))

if(choice == 1):
    print(bank.withdraw())

elif(choice == 2):
    print(bank.deposit())
    
elif(choice == 3):
    print(bank.statement())
    
else:
    print("Invalid Choice")
    
    
