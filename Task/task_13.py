# string methods a simple user login using string method

print("Create Id for Python Lecture")


name = input("Enter Your Name : ")

if (name.isalpha()):
    print(name)

    age = input("Enter Your Age : ")
    if (age.isdigit()):
        print(age)

        mail = input("Enter Your Mail ID : ")
        if (mail.islower()):
            print(mail)

            password = input("Create Password : ")
            if (password.isalnum()):

                confirm_password = input("Confirm Password : ")
                if(password == confirm_password):
                    print("Password Created Successfully")

                    mobile = input("Enter Mobile No. : ")
                    if(mobile.isdigit() and len(mobile) == 10):
                        print(mobile)
                        print()
                        print("Id has been created")
                    
                    else:
                        print("Wrong number input")
                        print("Enter only Numeric Value & Length should be 10 ")
                
                else:
                    print("password Doesn't match")
                    print("Enter Same Password")

            else:
                print("Password Requirement doesn't match")
                print("Enter AlphaNumeric Value")

        else:
            print("Wrong mail input")
            print("Enter letter in lower case")
    
    else :
        print("Wrong age input")
        print("Enter Only Numeric Value")


else:
    print("Wrong Name Input")
    print("Enter Only Alphabet's")
