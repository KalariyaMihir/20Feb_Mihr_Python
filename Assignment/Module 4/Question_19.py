# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.


print("\n--- Practically Applying Try/Except/Finally ---\n\n")

age = int(input('Enter an Value : '))

try:
    if (age > 18):
        print('-- You are Able to vote --')
    
    else:
        print('!OOPS You are not Eligible to Vote')

except Exception as e:

    print(e)

finally:
    print("Thank You for Visiting")
