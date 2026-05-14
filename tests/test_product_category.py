import pytest

from src.category import Category
from src.product import BaseProduct, Product, Grass, Smartphone


def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_creation():
    product = Product("iPhone", "Smartphone", 1000, 2)

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