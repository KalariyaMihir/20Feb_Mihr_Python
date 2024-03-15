# dynamic id,username input in list

id = []
name = []

student = int(input("Enter Number of Students : "))

for ind in range(student):
    no = input("Enter ID : ")
    id.append(no)

    for ind2 in range(1):
        nm = input("Enter Name : ")
        name.append(nm)



# id.extend(name)
print(id)
print(name)

for ind_no in range(student):

        print(f"Student {ind_no+1} : {name[ind_no]}")
