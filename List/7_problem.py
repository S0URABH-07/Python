# 
numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

k = k % len(numbers)

numbers[:] = numbers[-k:] + numbers[:-k]

print(numbers)