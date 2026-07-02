# Using Abstract Classes 
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car Started")

car = Car()
car.start()