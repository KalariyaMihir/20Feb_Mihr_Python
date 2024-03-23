# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged

print("\n--- This program is to add 'ing' in the end of the string ---\n\n")

string = input("Enter an string : ")
str2 = string



if(string.endswith('ing') ):
    
    print(f"\nOriginal String : {str2}")
    print(f"Updated String = {string.replace("ing",'ly')}")
    
elif(len(string) < 3):
    print(f"\nOriginal String : {str2}")
    print("Length of String is Less then 3 Character so it Remains Same")
    print(string)

else : 
    print(f"\nOriginal String : {str2}")
    print(f"Updated String = {string + 'ing'}")