# Make a result of student 

name = input("Enter Name of Students : ")

HTML = int(input("Enter Marks of HTML : "))
CSS = int(input("Enter Marks of CSS : "))
JS = int(input("Enter Marks of JS : "))
BS = int(input("Enter Marks of BS : "))
jQuery = int(input("Enter Marks of jQuery : "))

total = HTML + CSS + JS + BS + jQuery

pr = (total / 500)*100

print(f"\nName of Student is {name}")
print(f"Total Mark is : {total}.")
print(f"Your Percentage is : {pr}.")


if pr>=90:
    print("Pass With Grade A")

elif pr>75:
    print("Pass with Grade B")

elif pr>60:
    print("Pass with Grade C")

elif pr>50:
    print("Pass with Grade D")

elif pr<35:
    print(f"{name} has failed the exam.")


