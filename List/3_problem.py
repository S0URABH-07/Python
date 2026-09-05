# Find the missing number

numbers = [1,2,3,5,6,7]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
print("Missing Number: ",missing)