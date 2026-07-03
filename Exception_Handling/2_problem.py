# Exception Handling 
# else runs only if no exception occurs.
try:
    number = int(input("Enter Number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter only numbers")

else:
    print("Everything executed successfully")