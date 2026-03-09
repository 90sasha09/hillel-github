class Item:
    def __init__(self, name, price, description="", dimensions=""):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # словник {Item: кількість}

    def add_item(self, item, cnt):

        self.products[item] = cnt

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)



lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)  # lemon, price: 5
print(apple)  # apple, price: 2

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())  # 60


cart.add_item(apple, 10)
print(cart)
print(cart.get_total())  # 40
