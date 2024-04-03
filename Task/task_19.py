# Create an dynamic nested dictionary

tops = {}

# this is for get numbers of keys
value = int(input("Enter Numbers of Keys : "))

for num in range(value):
    
    child_key = str(input("Enter a Key : "))
    
    tops[child_key] = {}

    id = input("Enter Id of Student : ")
    name = input("Enter Name of Student : ")
    
    tops[child_key]["Name"]= name
    tops[child_key]["Name"]= id

    
print(tops)
    