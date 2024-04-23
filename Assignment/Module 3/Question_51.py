# Write a Python function that checks whether a passed string is palindrome or not

print("\n--- Thi Program is to check given string is palindrome or not ---\n\n")

string = input("Enter an String : ")

# string = '/

def palindrome(word):
    
    rev = word[-1::-1]
    
    if (word == rev):
        print(f"{word} is Palindrome.")
    else:
        print(f"{word} is not Palindrome.")
      
palindrome(string)
