# library for creating an bank account

import random

def details():
    global balance,holder_name,mobile_no,account_no,account_type
    
    holder_name = input("Enter Your Name : ")
    # holder_name = 'Mihir'

    mobile_no = int(input("Enter Your mobile NO. : ")) 
    # mobile_no = 3249846

    account_no = random.randrange(10000000,99999999)
    
    account_type = 'saving'
    
    balance = 10000
    
    
# details()
