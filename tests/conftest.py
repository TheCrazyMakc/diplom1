import pytest

from praktikum.burger import Burger
from helpers import (
    create_mock_bun,
    create_mock_ingredient,
    BUN_NAME_1,
    BUN_NAME_2,
    BUN_PRICE_1,
    BUN_PRICE_2,
    SAUCE_NAME,
    SAUCE_PRICE,
    FILLING_NAME,
    FILLING_PRICE,
    SAUCE_TYPE,
    FILLING_TYPE,
)


@pytest.fixture
def burger():
    """Пустой бургер без булочки и ингредиентов."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Мок булочки с дефолтными значениями."""
    return create_mock_bun(BUN_NAME_1, BUN_PRICE_1)


@pytest.fixture
def mock_bun_2():
    """Второй мок булочки — для проверки перезаписи."""
    return create_mock_bun(BUN_NAME_2, BUN_PRICE_2)


@pytest.fixture
def mock_sauce():
    """Мок соуса."""
    return create_mock_ingredient(SAUCE_NAME, SAUCE_PRICE, SAUCE_TYPE)


@pytest.fixture
def mock_filling():
    """Мок начинки."""
    return create_mock_ingredient(FILLING_NAME, FILLING_PRICE, FILLING_TYPE)