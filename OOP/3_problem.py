# Constructor (__init__) with parameters
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Sourabh", 22)
student2 = Student("Rahul", 21)

print(student1.name,student1.age)
print(student2.name,student2.age)