# Write a Python program to test whether a passed letter is a vowel or not.

print("--- This Program is t find that given letter is Vowel or Consent ---\n\n")

letter = input("Enter a single Character : ")

if(letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
    print(f"{letter} is Vowel.")

elif(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
    print(f"{letter} is Vowel.")

else:
    print(f"{letter} is Consent, Special Character or Number.")

