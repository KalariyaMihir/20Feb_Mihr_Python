# add users value in keys of dictionary

user = {"name"  : None,"city" : None,"course" : None}



for v in user.keys():
    
    user[v] = input(f"Enter Value of {v} : ")

print(user.keys())