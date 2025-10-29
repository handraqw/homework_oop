class Product:
    """Класс товара в онлайн-магазине."""

    def __init__(self, name, price, stock, category):
        """
        Инициализация продукта.
        name: название товара
        price: цена товара
        stock: количество на складе
        category: категория товара
        """

        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        """Информация о товаре с его характеристиками."""

        return f"{self.name} ({self.category}) - {self.price}₽, в наличии: {self.stock}"


class ShoppingCart:
    """Класс корзины покупателя."""

    def __init__(self):
        """Инициализация пустой корзины."""

        self.items = {}

    def add_product(self, product, quantity=1):
        """
        Добавление товара в корзину.
        product: объект Product
        quantity: количество
        """

        if product.stock < quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product):
        """
        Удаление товара из корзины.
        product: объект Product
        """

        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        """
        Обновление количества товара в корзине.
        product: объект Product
        quantity: новое количество
        """

        if product.stock < quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
        if quantity <= 0:
            self.remove_product(product)
        else:
            self.items[product] = quantity

    def total(self):
        """Возвращает общую стоимость товаров в корзине."""

        return sum(product.price * qty for product, qty in self.items.items())


class Order:
    """Класс заказа, включает расчёт стоимости с налогами и скидками."""

    TAX_RATE = 0.1
    DISCOUNT_RATE = 0.05

    def __init__(self, customer, cart):
        """
        Инициализация заказа.
        customer: объект Customer
        cart: объект ShoppingCart
        """

        self.customer = customer
        self.cart = cart
        self.total_price = self.calculate_total()
        self.is_completed = False

    def calculate_total(self):
        """Вычисляет итоговую сумму с учётом скидки и налога."""

        total = self.cart.total()
        total_with_discount = total * (1 - self.DISCOUNT_RATE)
        total_with_tax = total_with_discount * (1 + self.TAX_RATE)
        return round(total_with_tax, 2)

    def complete_order(self):
        """Оформление заказа: уменьшает склад, сохраняет заказ у покупателя."""

        for product, qty in self.cart.items.items():
            product.stock -= qty
        self.is_completed = True
        self.customer.orders.append(self)


class Customer:
    """Класс покупателя онлайн-магазина."""

    def __init__(self, name, email):
        """
        Инициализация покупателя.
        name: имя покупателя
        email: электронная почта
        """

        self.name = name
        self.email = email
        self.orders = []

