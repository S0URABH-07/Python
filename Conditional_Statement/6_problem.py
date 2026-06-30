balance = 5000
withdraw = int(input("Enter amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")