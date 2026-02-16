class Product:
    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} — {self.price}₽, {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"
