# Self problem 
class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def display(self):

        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)


student1 = Student("Sourabh",22,95)
student2 = Student("Rahul",21,88)

student1.display()

student2.display()