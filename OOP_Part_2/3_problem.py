# Protected variable in encapsulation with derive class
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"Private variable name is {self._name} and the age is {self._age}")

student = Student("Sourbh",21)
student.display_info()