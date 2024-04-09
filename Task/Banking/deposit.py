# library for deposit amount from account

import create

def deposit():

    amount = int(input("Enter Deposit Amount : "))
    
    if (amount < 2000):
        print("Minimum Deposit Amount should be more then 2000")
    
    elif(amount >= 2000):
        print(f"{amount} has Been Credited in your Account.")
    
    else:
        print("Invalid Input")
    
    return amount    

#deposit()
