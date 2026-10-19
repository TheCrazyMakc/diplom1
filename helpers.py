from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

# Названия и цены для тестовых данных
BUN_NAME_1 = "Test Bun 1"
BUN_NAME_2 = "Test Bun 2"
BUN_PRICE_1 = 50
BUN_PRICE_2 = 100

SAUCE_NAME = "Test Sauce"
SAUCE_PRICE = 20

FILLING_NAME = "Test Filling"
FILLING_PRICE = 40

SAUCE_TYPE = "SAUCE"
FILLING_TYPE = "FILLING"


def create_mock_bun(name: str = BUN_NAME_1, price: float = BUN_PRICE_1) -> Mock:
    """Создаёт мок булочки с заданными именем и ценой."""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock


def create_mock_ingredient(
    name: str = SAUCE_NAME,
    price: float = SAUCE_PRICE,
    ingredient_type: str = SAUCE_TYPE,
) -> Mock:
    """Создаёт мок ингредиента с заданными именем, ценой и типом."""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    mock.get_type.return_value = ingredient_type
    return mock