# Return 2 parameter in return

def student(id,name):
    
    return(id,name)

details = student(int(input("Enter Id : ")),input("Enter Name : "))

print(details[0])
