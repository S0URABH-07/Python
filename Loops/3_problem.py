# Triangle pattern
for i in range(1, 6):
    print("*" * i)


# Multiplication Table
num = int(input("Enter a number: "))
for j in range(1, 11):
    print(num, "x", j, "=", num * j)

# Sum of Numbers
total = 0

for k in range(1, 1001):
    total += k

print("Sum:", total)