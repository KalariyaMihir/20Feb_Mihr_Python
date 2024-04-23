# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

print("\n--- This Program is to set dictionary key as numbers between 1 to 15 ---\n\n")

student = {}

for i in range(1,16):
    student[i] = input(f"Enter Name Of {i} Student : ")

    
print(f"Your Dictionary : {student}")