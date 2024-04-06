# Creating a game Kaun Banega corerpati
# use list data type to store the questions and their correct answers
# display th final amount the people is taking home after plying the game.

print("\n--------------------- KAUN BANEGA CORERPATI ---------------------\n\n")

question = ['Which animal is known as the "Ship of the Desert"?',
            'Name the National animal of India?',
            'Name the National fruit of India?',
            'Which animal is known as the king of the jungle?',
            'Name the National bird of India?']
answer = ['camel','tiger','mango','lion','peacock']

money = 1000
increment = 2000
ind = 0
q_no = 1

for q in question:
    
    print(f"\nQuestion {q_no} : {q}")

    ans = input("Enter Answer : ")
        
    if(q <= question[3]):
        if(ans == answer[ind]):
            print(f"Amount is : {money}")
            money *= 2
            ind += 1
            q_no += 1
            # increment = increment * 2


            if(q == question[-1]):
                print(f"\nYour winning Amount is : {money}")
                print('You have completed this game')

        else:
            print("You Played Well")
            print(f"Your winning Amount is : {money}")
            break
        