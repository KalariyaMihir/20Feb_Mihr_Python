# When is the finally block executed?

print("\n--- When is the finally block executed? ---\n\n")

print("- Finally Block Executed in the end even try block has occurred with exception or without exception.")

try:
    a = '1'
    b = 5
    
    c = a+b

except (NameError, TypeError) as error:
    print(error)

else:
    print("Program is Complete")

    