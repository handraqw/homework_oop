class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}₽, в наличии: {self.stock}"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.stock < quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        if product.stock < quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
        if quantity <= 0:
            self.remove_product(product)
        else:
            self.items[product] = quantity

    def total(self):
        return sum(product.price * qty for product, qty in self.items.items())


class Order:
    TAX_RATE = 0.1
    DISCOUNT_RATE = 0.05

    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.total_price = self.calculate_total()
        self.is_completed = False

    def calculate_total(self):
        total = self.cart.total()
        total_with_discount = total * (1 - self.DISCOUNT_RATE)
        total_with_tax = total_with_discount * (1 + self.TAX_RATE)
        return round(total_with_tax, 2)

    def complete_order(self):
        for product, qty in self.cart.items.items():
            product.stock -= qty
        self.is_completed = True
        self.customer.orders.append(self)


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

