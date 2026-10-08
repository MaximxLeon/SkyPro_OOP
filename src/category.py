from src.product import Product
class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products: list[Product] = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def __str__(self):
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. "
            f"Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError(
                "Можно добавлять только объекты класса Product"
            )

    def middle_price(self):
        try:
            return sum(
                product.price for product in self.__products
            ) / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        return (
            f"Category('{self.name}', "
            f"products={self.products})"
        )