""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_info(self):
        return f"brand: {self.brand} model: {self.model} year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"brand: {self.brand} model: {self.model} year: {self.year} number_of_doorssd: {self.number_of_doors}"


car1 = Car("Toyota",model="Yaris",year="2008",number_of_doors=4)
car1 = Car("Toyota","Yaris","2008",4)
print(car1.get_info())