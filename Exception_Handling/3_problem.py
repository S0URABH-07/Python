# Finally block always Executes
# Even if an error occurs, the file is closed properly.
file = None

try:
    file = open("Interview_Q.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
        print("File closed")