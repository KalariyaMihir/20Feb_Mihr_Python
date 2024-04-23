# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

print("\n--- This Program is to count strings where the length of string is more then 2 and first and last character are same. ---\n\n")

value = int(input("Enter How many values you want to Enter : "))

list = []

for i in range(value):
    list.append(input("Enter an String : "))
print(list)

for str in list:
    
    if (len(str) >= 2 ):
        
        if(str[0] == str[-1]):
            
            print(str)


            
