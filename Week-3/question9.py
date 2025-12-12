#No9
class Vehicle:
    def __init__(self, brand, year: int):
        self.brand = brand
        self.year = year
    def info(self):
        return f'Vehicle brand: {self.brand} year: {self.year}'
    
class Car(Vehicle):
    def __init__(self, brand, year: int, model):
        super().__init__(brand, year)
        self.model = model
    def info(self):
        return f'Car brand: {self.brand} model: {self.model} year: {self.year}'

v1 = Vehicle("Bugatti", 2015)
car1 = Car("Toyota", 2018, "Vitz")

print(v1.info())
print(car1.info())