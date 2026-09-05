# Find the second largest element without sorting
numbers = [10,5,6,20,8,20,15,10]
largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif largest > num > second_largest:
        second_largest = num

if second_largest == float("-inf"):
    print("Second largest does not exist")

else:
    print("Largest:",largest)
    print("Second Largest:",second_largest)