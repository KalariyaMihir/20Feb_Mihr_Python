# Student Management System with using Concept of Core Python 

# ------------------ variable declaration

student = {}

# -------------------------------------------------
print("\n\t\t\t\t\t\t-------------------- Student Management System --------------------\n\n")

role_choice  = 'y'

while (role_choice == 'y' or role_choice == 'Y'):
   
    print("\t\tPress 1 : for Counselor")
    print("\t\tPress 2 : for Faculty")
    print("\t\tPress 3 : for Student\n")

    role = int(input("What Describes You the best : "))


        #                   ----------------------------------- Role of Counselor ----------------------------------- 
    if (role == 1):

        print("\t\t\t\t\t\t\t\t\t----- Welcome Counselor -----\n\n")

        print("\t\t1. Add Student")
        print("\t\t2. Remove Student")
        print("\t\t3. View All Student")
        print("\t\t4. View Specific Student\n")

        c_choice = 'y'

        while (c_choice == 'y' or c_choice == 'Y'):
            counselor_choice = int(input("\nEnter choice of Counselor : ")) 

            if (counselor_choice == 1):

                print("\t\t\t\t\t\t\t\t--------- Adding an New Student ---------\n\n")

                add_choice = 'y'
                key = 1
                while(add_choice == 'y') :

                    first_name = input("Enter First name : ")
                    last_name = input("Enter Last name : ")
                    contact_number = int(input("Enter contact number: "))

                    student_info = {
                                        "First Name": first_name,
                                        "Last Name": last_name,
                                        "Contact Number": contact_number,
                                        "Subjects": {}
                                    }

                    num_subjects = int(input("\nHow many subjects do you want to add ? "))

                    for i in range(num_subjects):
                        print(f"\nAdding subject {i + 1}:")
                        subject_name = input("Enter subject name: ")
                        marks = float(input(f"Enter marks of {subject_name} : "))
                        fees = float(input(f"Enter fees of {subject_name} : "))

                        student_info["Subjects"][subject_name] = {
                            "Marks": marks,
                            "Fees": fees
                        }

                    student1 = {key : student_info}
                    student.update(student1)

                    add_choice =  input("\nWant to add more Student (y/n) : ")
                    key += 1                   


            elif(counselor_choice == 2):
                print("\t\t\t\t\t\t\t\t--------- Removing an Student ---------\n\n")

                remove_student = int(input("\nEnter Serial Number of the Student : "))

                confirmation = input("\nDo You Want to Remove this Student (y/n) ? :")

                if (confirmation == 'y' or confirmation == 'Y'):
                    student.pop(remove_student) 
                    print("\n------- Student has been Removed ------")
                else:
                    print("\n------- Removing Process Terminated ------- ")



            elif(counselor_choice == 3):

                    print("\t\t\t\t\t\t\t\t\t\t\t------- View Student -------\n\n")
                    print(student)

                # view all student

            elif(counselor_choice == 4):

                print("\t\t\t\t\t\t\t\t------- View Specific Student -------\n\n")
                search_student = input("Enter Serial Number of the Student : ")

                print(student[search_student])



            else:
                print("!OOPS... Invalid Choice for Counselor")

            c_choice = input("Do You want to perform More Action (y/n) : ")





        #                                   ----------------------------------- Role of Faculty ----------------------------------- 
    elif(role == 2):
        print("\t\t\t\t\t\t\t\t\t----- Welcome Faculty -----\n\n")

        print("\t\t1. Python")
        print("\t\t2. Java")
        print("\t\t3. Web Design")
        print("\t\t4. React JS\n")

        faculty_subject = input("Which subject do you teach? ").strip()

        f_choice = 'y'
        while f_choice.lower() == 'y':
            print("\t\t1. Add/Update Marks")
            print("\t\t2. View Students by Subject\n")

            faculty_choice = int(input("Enter choice of Faculty: "))

            if faculty_choice == 1:
                student_id = int(input("Enter Student Serial Number: "))
                
                if student_id in student:
                    if faculty_subject in student[student_id]["Subjects"]:
                        new_marks = float(input(f"Enter new marks for '{faculty_subject}': "))
                        student[student_id]["Subjects"][faculty_subject]["Marks"] = new_marks
                        print(f"Updated marks for '{faculty_subject}' to {new_marks}")
                    else:
                        print(f"Student {student_id} does not study '{faculty_subject}'")
                else:
                    print("Student not found.")

            elif faculty_choice == 2:
                print(f"Students studying '{faculty_subject}':")

                found_students = False
                for student_id, student_data in student.items():
                    if faculty_subject in student_data["Subjects"]:
                        student_name = f"{student_data['First Name']} {student_data['Last Name']}"
                        marks = student_data["Subjects"][faculty_subject]["Marks"]
                        print(f"Student {student_id}: {student_name} - Marks: {marks}")
                        found_students = True

                if not found_students:
                    print(f"No students found for subject '{faculty_subject}'.")

            f_choice = input("Do you want to perform more actions (y/n)?: ")









        # ----------------------------------- Role of Student ----------------------------------- 
    elif(role == 3):
        print("for Student")
        
        contact_number = int(input("Enter your contact number: "))
        
        found = False
        for key, student_info in student.items():
            if student_info["Contact Number"] == contact_number:
                print(f"Your details:\n{student_info}")
                found = True
                break
        
        if not found:
            print("No student found with this contact number.")

    else:
        print("---!OOPS Invalid Choice of Role ---")
        
    role_choice = input("Do You want to switch Your Role (y/n) : ")
    