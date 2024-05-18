rang = int(input("Enter Range : "))
# rang = 6

val = 0

for i in range(rang):

    for k in range(rang,i,-1):
        
        val += 1
        
        

for i in range(rang):
    
    for j in range(rang,i,-1):
        
        print(val,end=" ")
        val -= 1
        
    print("")
