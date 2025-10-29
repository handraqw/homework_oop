class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def description(self):
        return f"Транспортное средство: {self.brand} {self.model}"
    
class Car(Vehicle):
    def description(self):
        return f"Автомобиль: {self.brand} {self.model} — удобен для личных поездок"
    

class Bike(Vehicle):
    def description(self):
        return f"Велосипед: {self.brand} {self.model} — мобилен и полезен"
    

class Motorcycle(Vehicle):
    def description(self):
        return f"Мотоцикл: {self.brand} {self.model} — быстр и манёврен"
    

transport_car = Car("Toyota", "Camry")
transport_bike = Bike("Trek", "FX 3")
transport_motorcycle = Motorcycle("Yamaha", "R6")

print(transport_car.description())
print(transport_bike.description())
print(transport_motorcycle.description())
