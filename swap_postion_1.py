s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Swap the characters at index 1
new1 = s2[1] + s1[1:]
new2 = s1[1] + s2[1:]

result = new1 + " " + new2

print(result)