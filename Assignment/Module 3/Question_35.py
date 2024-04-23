# How Do You Traverse Through A Dictionary Object In Python?

print("\n--- This Program is for Traversing through an dictionary ---\n\n")

employee = {'id' : 101,
            'Name' : 'Mihir',
            'Job Title' : 'Software Developer',
            'salary' : 1200000}

for i in employee.items():
    print(i)