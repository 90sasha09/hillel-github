class Product:
    def __init__(self, name, price, description="", dimensions=""):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} - {self.price} грн"


class Customer:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, тел: {self.phone}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}  # словник {товар: кількість}

    def add_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def __str__(self):
        lines = [f"Замовлення для: {self.customer}"]
        for product, quantity in self.items.items():
            lines.append(f"{product} x {quantity}")
        lines.append(f"Сумарна вартість: {self.total_price()} грн")
        return "\n".join(lines)

__________