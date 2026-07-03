# Nested try-except
# You can place one try-except inside another.
try:
    print("Outer Try")

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Exception")

except:
    print("Outer Exception")