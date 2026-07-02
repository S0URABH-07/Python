# Private variable in encapsulation
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"Private variable name is {self.__name} and the age is {self.__age}")

student = Person("Sourbh",21)
student.display_info()