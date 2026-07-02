# Multilevel Inheritence 
class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def grok(self):
        print("Grok")


class Dog(Mammal):
    pass

dog = Dog()
dog.eat()
dog.grok()