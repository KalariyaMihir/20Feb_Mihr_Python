# When will the else part of try-except-else be executed?

print("\n--- When will the else part of try-except-else be executed? ---\n\n")

print("""
      - In Try-Except-Else else part will be executed if try part will get execute without any exception.
      - If any Exception occurs then else part will be not executed.\n\n""")

print("---------------------------------------------------------------------------------------------------------------------------\n\n")


print("Example : Enter Numbers for Division \n")
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

try:
    c = a/b
    
except:
    print("Numbers Can't Divide by Zero")
    
else:
    print(f"Answer is : {c}")