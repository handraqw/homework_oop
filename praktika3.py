class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}₽, в наличии: {self.stock}"

