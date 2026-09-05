# Find Pairs with a given sum
numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = set()
pairs = []

for num in numbers:

    complement = target - num

    if complement in seen:
        pairs.append((complement, num))

    seen.add(num)

print("Pairs:", pairs)