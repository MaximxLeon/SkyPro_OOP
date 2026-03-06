from .product import Product


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

    @property
    def products(self):
        """Геттер для просмотра списка товаров в виде одной строки"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def add_product(self, product: Product):
        """Добавляет продукт в категорию
        и увеличивает общий счётчик продуктов."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError(
                "Можно добавлять только объекты класса Product"
            )

    def __str__(self):
        products_str = ", ".join([str(p) for p in self.products])
        return (
            f"Category: {self.name}\n"
            f"Description: {self.description}\n"
            f"Products: {products_str}"
        )

    def __repr__(self):
        return f"Category('{self.name}', products={self.products})"
