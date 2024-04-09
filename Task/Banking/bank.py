# library for creating an bank account

import random

    
    
holder_name = input("Enter Your Name : ")

mobile_no = int(input("Enter Your mobile No. : ")) 

account_type = 'saving'

account_no = random.randrange(10000000,99999999)
    
balance = 10000
    
# ------------------------------------------------------------------------------------

# library for deposit amount from account

def deposit():
    global balance
    d_amount = int(input("Enter Deposit Amount : "))
    
    if (d_amount < 2000):
        print("Minimum Deposit Amount should be more then 2000")
    
    elif(d_amount >= 2000):
        balance = balance + d_amount
        print(f"{d_amount} Credited to your ")
    
    else:
        print("Invalid Input")

    return(f"Account Balance : {balance}")

# ------------------------------------------------------------------------------------
# withdraw function

def withdraw():
    
    global balance
    
    w_amount = int(input("Enter Your Withdraw amount : "))
    
    if(w_amount >= balance):
        print("--- Inefficient Balance ---")
    
    elif(w_amount <= balance):
        balance = balance - w_amount
        print(f"{w_amount} Debited from your Account.")
        
    else:
        print("Invalid input")
    
    return(f"Account Balance : {balance}")

# ------------------------------------------------------------------------------------

# statement of your bank account

def statement():
    print(f"Holders Name : {holder_name}")
    print(f"Account No. : {account_no}")
    print(f"Mobile No. : {mobile_no}")
    print(f"Account Type : {account_type}")
    print(f"Account Balance : {balance}")

statement()

