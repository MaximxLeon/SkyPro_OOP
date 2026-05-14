import pytest

from src.category import Category
<<<<<<< HEAD
from src.product import BaseProduct, Product, Grass, Smartphone
=======
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone
>>>>>>> origin/main


def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_creation():
    product = Product("iPhone", "Smartphone", 1000, 2)

<<<<<<< HEAD
    assert product.name == "iPhone"
    assert product.get_description() == "Smartphone"
    assert product.get_price() == 1000


def test_smartphone_is_product():
    phone = Smartphone("Samsung", "Phone", 500, 1)

    assert isinstance(phone, Product)
    assert phone.get_price() == 500


def test_grass_is_product():
    grass = Grass("Green", "Lawn grass", 50, 10)

    assert isinstance(grass, Product)
    assert grass.get_description() == "Lawn grass"


def test_add_products():
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)

    result = p1 + p2

    assert result == (100 * 2) + (200 * 3)


def test_price_setter():
    product = Product("A", "desc", 100, 1)

    product.price = 200
    assert product.price == 200


def test_price_setter_invalid(capsys):
    product = Product("A", "desc", 100, 1)

    product.price = -10
    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100  # не изменился


def test_repr_and_str():
    product = Product("A", "desc", 100, 1)

    assert "Product(" in repr(product)
    assert "A" in str(product)
=======
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
>>>>>>> origin/main
