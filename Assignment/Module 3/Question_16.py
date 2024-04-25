# Write a Python program to check whether a list contains a sub list

colors = ['Red', ['Black'], 'Green', 'Blue', 'Yellow']

for i in colors:
    if (type(i) == list):
        print("This List Contains the sub list")
    
    else:
        print("No This list doesn't contain any sub list.")
        
        
    