# Write python program that swap two number with temp variable and without temp variable

print("\n--- This is Program is to swap two values suing third variable and without third variable ---\n\n")

choice = input("Enter With for With variable & without for Without Variable : ")

if (choice == "With" or choice == "with"):

    print("--- With using Third Variable ---\n")

    number1 = input("Enter First Number : ")
    number2 = input("Enter Second Number : ")

    print(f"\nFirst value is : {number1}")
    print(f"Second Value is : {number2}\n")

    temp = number1
    number1 = number2
    number2 = temp

    print("-- After Swapping --\n")
    print(f"First Value is : {number1}")
    print(f"Second Value is : {number2}\n")

elif(choice == "Without" or choice == "without"):

    print("--- without using third variable ---")

    number_1 = input("Enter First Number : ")
    number_2 = input("Enter Second Number : ")

    print(f"\nFirst value is : {number_1}")
    print(f"Second Value is : {number_2}\n")

    number_1,number_2 = number_2,number_1

    print("-- After Swapping --\n")
    print(f"First Value is : {number_1}")
    print(f"Second Value is : {number_2}\n")

else:
    print("You have Entered Wrong Keyword")




