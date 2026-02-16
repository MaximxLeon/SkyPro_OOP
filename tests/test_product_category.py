import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product("iPhone 15", "Смартфон Apple", 120000.0, 5)


@pytest.fixture
def product_2():
    return Product("Samsung S24", "Смартфон Samsung", 110000.0, 3)


@pytest.fixture
def category_with_products(product_1, product_2):
    # Перед созданием сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    return Category(
        "Смартфоны",
        "Разные модели смартфонов",
        [product_1, product_2]
    )


def test_product_initialization(product_1):
    assert product_1.name == "iPhone 15"
    assert product_1.description == "Смартфон Apple"
    assert product_1.price == 120000.0
    assert product_1.quantity == 5


def test_product_str(product_1):
    assert str(product_1) == "iPhone 15 — 120000.0₽, 5 шт."


def test_product_repr(product_1):
    assert repr(product_1) == "Product('iPhone 15', 120000.0, 5)"


def test_category_initialization(category_with_products):
    assert category_with_products.name == "Смартфоны"
    assert category_with_products.description == "Разные модели смартфонов"
    assert len(category_with_products.products) == 2


def test_category_counter(category_with_products):
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories(product_1, product_2):
    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    Category("Смартфоны", "Описание", [product_1])
    Category("Ноутбуки", "Описание", [product_2])

    assert Category.category_count == 2
    assert Category.product_count == 2
