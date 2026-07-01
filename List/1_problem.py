marks=[]

for i in range(5):
    mark=int(input("Enter Marks: "))
    marks.append(mark)

print("Marks:",marks)

print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Average:",sum(marks)/len(marks))