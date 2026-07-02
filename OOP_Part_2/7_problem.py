# Call super function 
class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")

dog = Dog()