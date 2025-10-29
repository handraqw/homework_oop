class Vehicle:
    """Родительский класс для транспортных средств"""

    def __init__(self, brand, model):
        """
        Инициализация транспортного средства.
        brand: марка/производитель
        model: модель транспортного средства
        """

        self.brand = brand
        self.model = model
    
    def description(self):
        """"Информация о транспортном средстве"""

        return f"Транспортное средство: {self.brand} {self.model}"
    
class Car(Vehicle):
    """Класс автомобиля, наследует Vehicle."""

    def description(self):
        """"Информация о транспортном средстве"""

        return f"Автомобиль: {self.brand} {self.model} — удобен для личных поездок"
    

class Bike(Vehicle):
    """Класс велосипеда, наследует Vehicle."""

    def description(self):
        """"Информация о транспортном средстве"""

        return f"Велосипед: {self.brand} {self.model} — мобилен и полезен"
    

class Motorcycle(Vehicle):
    """Класс мотоцикла, наследует Vehicle."""
    
    def description(self):
        """"Информация о транспортном средстве"""

        return f"Мотоцикл: {self.brand} {self.model} — быстр и манёврен"
    

transport_car = Car("Toyota", "Camry")
transport_bike = Bike("Trek", "FX 3")
transport_motorcycle = Motorcycle("Yamaha", "R6")

print(transport_car.description())
print(transport_bike.description())
print(transport_motorcycle.description())
