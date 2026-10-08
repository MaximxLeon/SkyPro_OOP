import pytest

from src.category import Category
from src.product import BaseProduct, Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_creation():
    product = Product("iPhone", "Smartphone", 1000, 2)

    assert product.name == "iPhone"
    assert product.get_description() == "Smartphone"
    assert product.get_price() == 1000


def test_smartphone_is_product():
    phone = Smartphone(
        "Samsung",
        "Phone",
        500,
        1,
        90.0,
        "S23",
        256,
        "Black"
    )

    assert isinstance(phone, Product)
    assert phone.get_price() == 500


def test_grass_is_product():
    grass = LawnGrass(
        "Green",
        "Lawn grass",
        50,
        10,
        "Russia",
        "7 days",
        "Green"
    )

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
    assert product.price == 100


def test_repr_and_str():
    product = Product("A", "desc", 100, 1)

    assert "Product(" in repr(product)
    assert "A" in str(product)


def test_product_zero_quantity():
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product(
            "Бракованный товар",
            "Неверное количество",
            1000.0,
            0
        )


def test_middle_price():
    product1 = Product("Товар 1", "Описание 1", 1000.0, 5)
    product2 = Product("Товар 2", "Описание 2", 2000.0, 3)
    product3 = Product("Товар 3", "Описание 3", 3000.0, 2)

    category = Category(
        "Категория",
        "Описание категории",
        [product1, product2, product3]
    )

    assert category.middle_price() == 2000.0


def test_middle_price_empty_category():
    category = Category(
        "Пустая категория",
        "Категория без продуктов",
        []
    )

    assert category.middle_price() == 0