""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    def __init__(self, brand, modle, year):
        self.brand = brand
        self.modle = modle
        self.year = year

    def get_info(self):
        return f"brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self): #overriding method
        return f"brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.number_of_doors}"
myCar = Car("Toyota", "Yaris Cross", 2025, 4)
print(myCar.get_info())