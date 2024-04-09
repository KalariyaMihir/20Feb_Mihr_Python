# Create an banking system using library and package

from Banking import bank

print("""
      1 : Withdraw Money
      2 : Deposit Money 
      3 : Print Statement\n
      """)

ch = 'y'

while ch == 'y':

    choice = int(input("Enter Your Choice : "))

    if(choice == 1):
        print(bank.withdraw(),"\n")

    elif(choice == 2):
        print(bank.deposit(),"\n")

    elif(choice == 3):
        print(bank.statement(),"\n")

    else:
        print("Invalid Input")

    ch = input("Press y to perform more operation : ")
    
    if (ch != 'y'):
        break
    
    else:
        print("Your Session is Ended")