class Category:
    category_count = 0        # общее количество категорий
    product_count = 0        # общее количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счётчики класса
        Category.category_count += 1
        # Добавляем количество продуктов этой категории
        Category.product_count += len(products)

    def __str__(self):
        products_str = ", ".join([str(p) for p in self.products])
        return f"Category: {self.name}\nDescription:\
            {self.description}\nProducts: {products_str}"

    def __repr__(self):
        return f"Category('{self.name}', products={self.products})"
