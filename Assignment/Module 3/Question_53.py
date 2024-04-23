# How can you pick a random item from a list or tuple?

import random 

print("\n--- This Program is used to choose the random items from a list or tuple ---\n\n")

color = ('Red', 'Green', 'Blue', 'White', 'Black', 'Orange')

pick = random.choice(color)

print(f"Tuple : {color}\n")
print(f"Random item from Tuple is : {pick}") 

