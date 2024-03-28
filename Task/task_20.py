# create udf of for multiple student entry

def detail(id,name,sub):
    print("Id :",id)
    print("Name :",name)
    print("Subject :",sub)

choice = int(input("Enter Number of Entries : "))

for i in range(choice):

    id = int(input("Enter ID : "))
    name = input("Enter Name of Student : ")
    sub = input("Enter Subject Name : ")
    
    detail(id,name,sub,"\n")
