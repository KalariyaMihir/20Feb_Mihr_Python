# create an bank management system using function
ac_no = int(input("Enter Acount Number : "))
name = input("Enter Acount Holder Name : ")
ac_type = input("Type of Acount (Saving / Current) : ")
balance = int(input("Enter Your Bank Balance : "))

def create():
    print(f"\nName : {name}")
    print(f"Acount No is : {ac_no}")
    print(f"Account Type : {ac_type}")
    print(f"Balance : {balance}")

def deposit():
    global balance
    amount = int(input("Enter Deposit Amount : "))
    
    if (amount < 2000):
        print("Deposit Value should be more then 2000") 
    
    else:
        balance =  balance + amount
        print(f"{amount} has been credited to your acount")
        
    statement()
        

def withdraw():
    global balance
    
    amount = int(input("Enter Withdrawal Amount : "))
    
    if(amount > balance):
        print("You have inefficient Balance")
        
    else:
        balance = balance - amount

        print(f"{amount} has been Debited from Your Acount")
        
    statement()
    
        

def statement():
    
    print("--------- Acount Summery ---------")
    create()

# --------------------------------------------------

print("\n-> Enter Deposit for Deposit")
print("-> Enter Withdraw for withdraw")
print("-> Enter Statement for see the Statement ")

choice = input("Enter Your Choice : ") 

if(choice == "Deposit" or choice == "deposit"):
    deposit()    

elif(choice == "Withdraw" or choice == "withdraw"):
    withdraw()

elif(choice == "Statement" or choice == "statement"):
    statement()  

else:
    print("Invalid Request")  
