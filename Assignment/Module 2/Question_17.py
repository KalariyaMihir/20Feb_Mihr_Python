# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

print("\n--- This Program is to print single string from two strings with space and swap the first character of each string ---\n\n")

str_1 = input("Enter First String : ")
str_2 = input("Enter Second String : ")

fn = str_1[0]
sn = str_1[1]

fn1 = str_2[0]
sn1 = str_2[1]

fn,sn = sn,fn
fn1,sn1 = sn1,fn1

str_3 = fn + sn + str_1[2:] +" "+ fn1 + sn1 + str_2[2:]  

print(str_3) 



