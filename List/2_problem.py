# Find all duplicate Element
numbers = [1,2,3,2,4,5,1,6,3]
seen = set()
duplicates = []

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)

    else:
        seen.add(num)

print("Duplicates: ",duplicates)