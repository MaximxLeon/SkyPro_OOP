class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для установки новой цены продукта."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, products: list):
        """Создаёт новый продукт или обновляет существующий."""

        for product in products:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                product.price = max(product.price, product_data["price"])
                return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __str__(self):
        return f"{self.name} — {self.price}₽, {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"