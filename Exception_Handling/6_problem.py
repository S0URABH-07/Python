# ATM Problem 
balance = 5000
try:
    amount = int(input("Enter withdrawal amount: "))

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

finally:
    print("Thank you for using our ATM.")