#  Write a Python program to read a random line from a file.
# import random

# file = open(r'D:\Full Stack\BE\Pyhotn\Assignment\Module 3\open.text','r')


# choose = file.readline()


# print(random.choice(choose[0:]))

# file.close

import random

def get_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        random_index = random.randint(0, num_lines - 1)
        return lines[random_index]

filename = r'D:\Full Stack\BE\Pyhotn\Assignment\Module 3\open.text'  # Replace 'your_file.txt' with the name of your file
random_line = get_random_line(filename)
print(f"Random line from the file : {random_line}")
