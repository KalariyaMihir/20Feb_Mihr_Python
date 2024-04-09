import create

def withdraw():
    
    amount = int(input("Enter Your Withdraw amount : "))
    
    if(amount >= create.balance):
        print("--- Inefficient Balance ---")
    
    elif(amount <= create.balance):
        print(create.balance - amount)
        
    else:
        print("Invalid input")
        

#withdraw()