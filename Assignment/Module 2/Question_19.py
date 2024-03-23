# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

string = "Ambani is not an poor Person"

st1 = string.find("not")
st2 = string.find("poor")
print(f"Fist Appearance of 'not' is start from index : {st1}")
print(f"Fist Appearance of 'poor' is start from index : {st2}")

print(string.replace(string[st1:st2+4],"good"))


