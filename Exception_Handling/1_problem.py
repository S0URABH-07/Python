# Exception Handling with multiple except block
try:
    number = int(input("Enter Number: "))
    print(100 / number)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide by Zero")