for i in range(2, 11, 2):
    print(i)

# Looping Through a string
name = "Python"
for ch in name:
    print(ch)

# Looping Through a list
numbers = [10, 20, 30, 40]
for n in numbers:
    print(n)

# Looping Through a Dictionary
student = {
    "name": "Sourabh",
    "age": 22,
    "course": "Python"
}
for key in student:
    print(key, ":", student[key])

j = 1
while j <= 5:
    print(j)
    j += 1