# Write a Python script to check if a given key already exists in a dictionary.

print("\n--- This Program is for find the given key is exists in dictionary or not ---\n\n") 

FullStack = {1: 'HTML', 2: 'CSS', 3: 'JS', 4: 'BootStrap', 5: 'jQuery', 6: 'C', 7: 'C++', 8: 'MySQL', 9: 'Python', 10: 'Django'}

word = int(input("Enter Key to find Values : ")) 

if word in FullStack.keys():
    
    print(f"{word} : {FullStack[word]}")
    
else :
    print("Not Found the matching key")