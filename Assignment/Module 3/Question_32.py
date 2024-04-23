# Write a Python script to sort (ascending and descending) a dictionary by value.

print("\n--- This Program is to sort dictionary value in Ascending or Descending order ---\n\n")

dict = {1 : 'Red',
        2 : 'Green',
        3 : 'Blue',
        4 : 'Yellow',
        5 : 'Black'}

ind = len(dict)
print(f"Dictionary : {dict}\n")
print("-- Enter a for Ascending and d for descending --")
choose = input("Enter Choice : ")

if (choose == 'a' or choose == 'A'):
    
    print("Dictionary in Ascending Order : ")
    for i in range(1, len(dict)+1):
        
        print(dict[i])
        
elif (choose == 'd' or choose == 'D'):
    
    print("Dictionary in Descending Order : ")
    for i in range(len(dict)):
        print(dict[ind])
        ind -= 1
        