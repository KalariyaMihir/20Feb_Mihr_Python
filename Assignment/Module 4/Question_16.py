# Can one block of except statements handle multiple exception?

print("\n--- Can one block of except statements handle multiple exception? ---\n\n")

print("Yes one block of except can handle multiple exceptions\n")

try:
    a = '1'
    b = 5
    
    c = a+b
except (NameError, TypeError) as error:
    print(error)
    
    