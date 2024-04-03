# create an nested dictionary in function

def nested_dict():
    
    tops = { }
    
    value = int(input("Enter how Many Entires you want : "))
    
    for i in range(value):
        
        parent_key = input("Enter an Course :")
        
        tops[parent_key] = {}

        

        entry = int(input(f"Entries of {parent_key} : "))

        
        for i in range(entry):
            id = input("Enter Id : ")
            name = input("Enter Name : ")
        
            tops[parent_key]["Id"]= id
            tops[parent_key]["Name"]= name
        
    print(tops)
    # return tops

nested_dict()
        
