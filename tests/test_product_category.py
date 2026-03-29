import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_product_repr(product_1):
    assert repr(product_1) == "Product('iPhone 15', 120000.0, 5)"


def test_category_initialization(category_with_products):
    assert category_with_products.name == "Смартфоны"
    assert category_with_products.description == "Разные модели смартфонов"
    assert category_with_products.products.count("\n") + 1 == 2


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


def test_price_setter_valid(product_1):
    product_1.price = 130000
    assert product_1.price == 130000


def test_price_setter_invalid(product_1, capsys):
    product_1.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_1.price == 120000.0


def test_new_product_create():
    data = {
        "name": "Xiaomi 14",
        "description": "Смартфон Xiaomi",
        "price": 90000.0,
        "quantity": 4
    }

    product = Product.new_product(data)

    assert product.name == "Xiaomi 14"
    assert product.description == "Смартфон Xiaomi"
    assert product.price == 90000.0
    assert product.quantity == 4


def test_add_product_to_category(category_with_products):
    new_product = Product("Xiaomi 13", "Смартфон Xiaomi", 80000.0, 6)
    category_with_products.add_product(new_product)
    assert category_with_products.products.count("\n") + 1 == 3


def test_product_addition():
    """Проверка корректного сложения двух продуктов"""
    p1 = Product("Товар 1", "", 100, 10)
    p2 = Product("Товар 2", "", 200, 2)

    assert p1 + p2 == 1400


def test_product_addition_type_error():
    """Проверка ошибки при сложении с неправильным типом"""
    p = Product("Товар", "", 100, 5)

    with pytest.raises(TypeError):
        p + 10


def test_product_addition_zero_quantity():
    """Проверка работы с нулевым количеством"""
    p1 = Product("Товар 1", "", 100, 0)
    p2 = Product("Товар 2", "", 200, 2)

    assert p1 + p2 == 400


# -------------------------
# 1. Наследование
# -------------------------

def test_smartphone_is_product():
    phone = Smartphone("iPhone", "", 1000, 5, 90, "15 Pro", 256, "black")
    assert isinstance(phone, Product)
    assert phone.efficiency == 90
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "black"


def test_lawn_grass_is_product():
    grass = LawnGrass("Green", "", 100, 10, "Russia", 7, "green")
    assert isinstance(grass, Product)
    assert grass.country == "Russia"
    assert grass.germination_period == 7
    assert grass.color == "green"


# -------------------------
# 2. Проверка __add__
# -------------------------

def test_add_same_class():
    p1 = Product("A", "", 100, 2)
    p2 = Product("B", "", 200, 3)

    assert p1 + p2 == 100 * 2 + 200 * 3


def test_add_different_classes_raises():
    phone = Smartphone("iPhone", "", 1000, 1, 90, "15", 128, "black")
    grass = LawnGrass("Grass", "", 100, 1, "RU", 5, "green")

    with pytest.raises(TypeError):
        phone + grass


# -------------------------
# 3. Category.add_product защита
# -------------------------

def test_add_valid_product_to_category():
    cat = Category("Test", "desc", [])
    product = Product("Test", "", 100, 1)

    cat.add_product(product)

    assert "Test" in cat.products


def test_add_invalid_object_to_category():
    cat = Category("Test", "desc", [])

    with pytest.raises(TypeError):
        cat.add_product("not a product")