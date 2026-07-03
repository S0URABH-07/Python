# Reading a CSV = Comma-Separated Values.
import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)