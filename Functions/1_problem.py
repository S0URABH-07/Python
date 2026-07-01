def greet():
    print("Welcome to Python")

greet()


# Function with Parameters
def greet(name):
    print("Hello", name)

greet("Sourabh")

# With parameters
def square(number):
    print(number * number)

square(5)


# Positional Argument
def student(name, age):
    print(name)
    print(age)

student("Sourabh", 22)

# Default Parameters ->>>>>>> You can provide default values.
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sourabh")


# print() displays the value but does not return it
# Use return when you want to reuse the result later.
def add(a, b):
    print("Using print",a+b)
    return a + b

result = add(5, 3)

print(result)

# Function Returning multiple value
def calculate(a, b):
    return a + b, a - b

sum_value, diff = calculate(10, 5)

print(sum_value)
print(diff)