# *args -->> Accepts multiple positional arguments.
def total(*numbers):
    print(sum(numbers))
    print(min(numbers))
    print(max(numbers))
    print(len(numbers))

total(10, 20, 30,1000000, 40)

# **kwargs -->> Accepts multiple keyword arguments.
def student(**details):
    print(details)

student(name="Sourabh", age=22)

# Function Documentation (Docstring)
def add(a, b):
    """Returns the sum
      of two numbers."""
    return a + b

print(add.__doc__)