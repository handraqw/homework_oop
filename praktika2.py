class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def description(self):
        return f"Транспортное средство: {self.brand} {self.model}"