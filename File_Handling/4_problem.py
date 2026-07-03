# Writing a CSV file
# This w erase all previous data than write
# Use "a" if you want to keep existing data.
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Sourabh", 22, 95])