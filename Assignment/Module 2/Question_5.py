#  What is the purpose continue statement in python?

print("\n- Continue Statement skip the given condition and continue the further process.\n\n")

print("Example : we are printing 1 to 10 numbers and skip number 5 ")


for ind in range(11):

    if(ind == 5):
        continue

    print(ind,end=", ")