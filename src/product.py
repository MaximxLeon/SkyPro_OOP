from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class MixinProduct:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self.__class__.__name__} -> {self}")


class Product(MixinProduct, BaseProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__()

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.description

    def __add__(self, other):
        if isinstance(other, Product):
            return (
                (self.__price * self.quantity) +
                (other.__price * other.quantity)
            )
        raise TypeError("Можно складывать только объекты Product")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __repr__(self):
        return (
            f"Product('{self.name}',\
            '{self.description}', {self.__price}, {self.quantity})"
        )


class Smartphone(Product):
    pass


class Grass(Product):
    pass
