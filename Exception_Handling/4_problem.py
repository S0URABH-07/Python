# Use raise keyword
# You can create your own Exceptions
class InsufficientBalance(Exception):
    pass

balance = 500
withdraw = 1000

if withdraw > balance:
    raise InsufficientBalance("Insufficient balance")