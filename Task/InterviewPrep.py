

# for i in range (1,6):
#     space = 1
    
#     for j in range(6,0,-1):
        
#         if j >i:
#             print(' ',end=" ")
#         else:
#             print('*',end=" ")
            
#             space += 1
#     print(" ")
    
    
#           *  
#         * *  
#       * * *  
#     * * * *  
#   * * * * *
    
    
# --------------------------------------------------------------------
    
    

# space1 = 5
# for i  in range(6):
    
#     for j in range(space1):
#         print(end="  ")
#     space1 -= 1 
    
#     for k in range(i):
#         print("*",end=" ")
        
#     print("")
    
    
    
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
    
# --------------------------------------------------------------------
    
    
# for i in range(1,6):
    
#     for j in range(1,i+1):
        
#         print(j,end=" ")
        
#     print("")
    
    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
    
# --------------------------------------------------------------------
    
    
# for i in range(1,50):
#         if True:
#             continue 
#         print('a')
        
#         break
#         print("b")
        
    # print nothing

# --------------------------------------------------------------------


# for i in range (1,6):                                  

#     for j in range(1,i+1):
#         print(1,end=" ")
    
#     print("")
    
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1

# --------------------------------------------------------------------
    
# sum = 0 

# for i in range(1,11):
#     if(i%2 == 0):
#         sum += i
# print(sum)                               #30

# --------------------------------------------------------------------

# for i in range(1,6):
#     for j in range(1,i+1):
        
#         print(j,end=" ")
    
#     print("")
    

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# --------------------------------------------------------------------

# for i in range(1,50):

#     if True:
#         print(1)
#         continue
    
#     print('a')
    
#     break

#     print('b')

# --------------------------------------------------------------------

# for i in range(5,0,-1):
    
#     for j in range(i):
#         print('*',end=" ")
        
#     print("")

# --------------------------------------------------------------------


# space = 5

# for i in range(1,6):
    
#     for j in range(space):
#         print(end="  ")
#     space -= 1
    
#     for k in range(1,i+1):
#         print(k,end=" ")
        
#     print("")
    
#           1 
#         1 2
#       1 2 3
#     1 2 3 4
#   1 2 3 4 5

# --------------------------------------------------------------------

# space = 5
# for i in range(1,6):
    
#     for j in range(space):
#         print(end="  ")
#     space-=1
    
#     for k in range(i,0,-1):
#         print(k,end=" ")
        
    
#     print("")
    
#           1 
#         2 1 
#       3 2 1 
#     4 3 2 1 
#   5 4 3 2 1

# --------------------------------------------------------------------

# space = 5

# for i in range(1,6):
    
#     for j in range(space):
#         print(end="  ")
#     space -= 1

#     for k in range(i,0,-1):
#         print(k,end=" ")
        
#     print("")
    
    
#           1 
#         2 1
#       3 2 1
#     4 3 2 1
#   5 4 3 2 1

# --------------------------------------------------------------------

# val = 12
# ans = val/4

# print(ans)
# for i in range(int(ans)):
    
#     for j in range(4):
        
#         print(val,end=" ")
#         val-=1
    
#     print("")
    
    
# 3.0
# 12 11 10 9
# 8 7 6 5
# 4 3 2 1
    
# --------------------------------------------------------------------

# num = int(input("Enter number to find Factorial : "))

# fact = 1

# for i in range(1,num):
    
#     fact*= i
    
# print(fact,end=", ")

# print factorial of number

# --------------------------------------------------------------------

# fibonacci = 10
# n1 = 0
# n2 = 1
# n3 : int
# for i in range(2,fibonacci+1):

#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3

# print(n3)

# print fibonacci 

# --------------------------------------------------------------------

# num = 30
# for i in range(2,num):
    
#     if(i%i == 0 and i%2 != 0):
#         print(i)
    
# --------------------------------------------------------------------

# space = 5
# for i in range(1,6):
    
#     for j in range(space):
        
#         print(end="  ")
#     space -= 1
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     print("")


# --------------------------------------------------------------------

space = 5

for i in range(1,6):
    
    for j in range(space):
        print(end=" ")
    space -= 1
    
    for k in range(i):
        print(i,end=" ")
    print("")

# --------------------------------------------------------------------



# --------------------------------------------------------------------
# --------------------------------------------------------------------

    


# # import multiprocessing.process
# import time
# import multiprocessing

# # center = Faculty()

# def number():
#     row = 6
#     for i in range(1,6):

#         num = 1

#         for j in range(row,0,-1):

#             if(j>i):
#                 print(end="  ")
#             else:
#                 print(num,end=" ")
#                 num += 1        

#         print("")
#         time.sleep(1)



# def numbers():

#     space = 4

#     for i in range(1,6):

#         for j in range(space):

#             print(end="  ")

#         space -=1


#         for k in range(i):

#             print(k+1,end=" ")
#         print("")
#         time.sleep(1)    
        
        
# if __name__ == '__main__':
    
#     process_1 = multiprocessing.Process(target = number)
#     process_2 = multiprocessing.Process(target = numbers)

#     process_1.start()
#     process_2.start()

#     process_1.join()
#     process_2.join()
    
#     print('Done')

# --------------------------------------------------------------------

dict = {}

for i in range(1,6):
    
    dict[i] = i*i
    
print(dict)

dict = {i: chr(64+i) for i in range(1,6) }

print(dict)