tpl = []

val = int(input("Enter Number of Value : "))

for ind in range(1,val+1):

    number = input("Enter value : ") 
    tpl.append(number)

print(tuple(tpl))