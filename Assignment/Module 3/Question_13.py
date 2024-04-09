# Write a Python program to select an item randomly from a list.

import random
print("\n--- This Program is return random values from list ---\n\n")

list = ['Red','Green','Blue','Pink','Orange','Black']

print(f"Your List is : {list}")

print(f"Random Values from List is : {random.choice(list)}")

