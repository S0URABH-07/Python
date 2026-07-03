# Using With Keyword
with open("Notes.txt", "r") as file:
    print(file.read(50))
    print(file.read(5))
    print(file.tell())