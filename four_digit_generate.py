import math

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))
result = []

for num in range(start, end + 1):
    if 1000 <= num <= 9999:
        if all(int(d) % 2 == 0 for d in str(num)):
            root = int(math.sqrt(num))
            if root * root == num:
                result.append(num)

print("Number that satisfy the condition:", result)