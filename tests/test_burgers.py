import pytest

from praktikum.burger import Burger
from helpers import (
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


class TestSetBuns:
    """Тесты метода set_buns."""

    def test_set_buns_sets_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_set_buns_overwrites_previous_bun(self, burger, mock_bun, mock_bun_2):
        burger.set_buns(mock_bun)
        burger.set_buns(mock_bun_2)
        assert burger.bun == mock_bun_2

    def test_set_buns_returns_none(self, burger, mock_bun):
        assert burger.set_buns(mock_bun) is None


class TestAddIngredient:
    """Тесты метода add_ingredient."""

    def test_add_one_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_add_two_ingredients_preserves_order(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.ingredients == [mock_sauce, mock_filling]

    @pytest.mark.parametrize("count", [1, 2, 3, 5, 10])
    def test_add_many_ingredients(self, burger, mock_sauce, count):
        for _ in range(count):
            burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == count

    def test_add_two_same_ingredients(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce, mock_sauce]

    def test_add_ingredient_returns_none(self, burger, mock_sauce):
        assert burger.add_ingredient(mock_sauce) is None


class TestRemoveIngredient:
    """Тесты метода remove_ingredient."""

    def test_remove_only_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_first_of_two(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    def test_remove_last_of_two(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_sauce]

    def test_remove_middle_of_three(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_sauce, mock_sauce]

    def test_remove_from_empty_raises_index_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_remove_with_invalid_index_raises_index_error(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_remove_with_negative_index(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(-1)
        assert burger.ingredients == [mock_sauce]

    def test_remove_ingredient_returns_none(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.remove_ingredient(0) is None


class TestMoveIngredient:
    """Тесты метода move_ingredient."""

    def test_move_first_to_second(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    def test_move_second_to_first(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_filling, mock_sauce]

    def test_move_same_position_does_nothing(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 0)
        assert burger.ingredients == [mock_sauce, mock_filling]

    def test_move_first_to_end_of_three(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)   # 0
        burger.add_ingredient(mock_filling) # 1
        burger.add_ingredient(mock_sauce)   # 2
        burger.move_ingredient(0, 2)
        # pop(0) -> [filling, sauce], insert(2, sauce) -> [filling, sauce, sauce]
        assert burger.ingredients == [mock_filling, mock_sauce, mock_sauce]

    def test_move_last_to_first_of_three(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)   # 0
        burger.add_ingredient(mock_filling) # 1
        burger.add_ingredient(mock_sauce)   # 2
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock_sauce, mock_sauce, mock_filling]

    def test_move_with_invalid_index_raises_index_error(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    def test_move_ingredient_returns_none(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.move_ingredient(0, 1) is None


class TestGetPrice:
    """Тесты метода get_price."""

    def test_get_price_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == BUN_PRICE_1 * 2

    def test_get_price_with_bun_and_one_sauce(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == BUN_PRICE_1 * 2 + SAUCE_PRICE

    def test_get_price_with_bun_and_one_filling(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == BUN_PRICE_1 * 2 + FILLING_PRICE

    def test_get_price_with_bun_and_two_ingredients(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected = BUN_PRICE_1 * 2 + SAUCE_PRICE + FILLING_PRICE
        assert burger.get_price() == expected

    def test_get_price_without_bun_raises_attribute_error(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_price_without_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == BUN_PRICE_1 * 2

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (50, [20], 120),                # 50*2 + 20
            (50, [20, 40], 160),            # 50*2 + 20 + 40
            (100, [10, 10, 10], 230),       # 100*2 + 30
            (0, [20, 40], 60),              # 0*2 + 60
            (50, [], 100),                  # 50*2
            (50, [0], 100),                 # 50*2 + 0
            (0, [], 0),                     # 0
            (50, [100, 200, 300], 700),     # 50*2 + 600
        ],
    )
    def test_get_price_parametrized(self, burger, bun_price, ingredient_prices, expected):
        from helpers import create_mock_bun, create_mock_ingredient
        mock_bun = create_mock_bun(BUN_NAME_1, bun_price)
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            burger.add_ingredient(create_mock_ingredient(SAUCE_NAME, price))
        assert burger.get_price() == expected


class TestGetReceipt:
    """Тесты метода get_receipt."""

    def test_get_receipt_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected = f"(==== {BUN_NAME_1} ====)\n(==== {BUN_NAME_1} ====)\n\nPrice: {BUN_PRICE_1 * 2}"
        assert receipt == expected

    def test_get_receipt_with_one_sauce(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert f"= sauce {SAUCE_NAME} =" in receipt

    def test_get_receipt_with_one_filling(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert f"= filling {FILLING_NAME} =" in receipt

    def test_get_receipt_contains_bun_name(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert BUN_NAME_1 in receipt

    def test_get_receipt_contains_price(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        expected_price = BUN_PRICE_1 * 2 + SAUCE_PRICE
        assert f"Price: {expected_price}" in receipt

    def test_get_receipt_structure(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        lines = receipt.split("\n")
        assert lines[0] == f"(==== {BUN_NAME_1} ====)"
        assert lines[1] == f"= sauce {SAUCE_NAME} ="
        assert lines[2] == f"= filling {FILLING_NAME} ="
        assert lines[3] == f"(==== {BUN_NAME_1} ====)"
        assert lines[4] == ""
        assert lines[5] == f"Price: {BUN_PRICE_1 * 2 + SAUCE_PRICE + FILLING_PRICE}"

    def test_get_receipt_ingredient_type_lowercased(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "sauce" in receipt
        assert "SAUCE" not in receipt

    def test_get_receipt_without_bun_raises_attribute_error(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_returns_string(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert isinstance(burger.get_receipt(), str)

    @pytest.mark.parametrize(
        "ingredient_type, expected_prefix",
        [
            (SAUCE_TYPE, "= sauce"),
            (FILLING_TYPE, "= filling"),
        ],
    )
    def test_get_receipt_ingredient_type_parametrized(
        self, burger, mock_bun, ingredient_type, expected_prefix
    ):
        from helpers import create_mock_ingredient
        mock = create_mock_ingredient("Test", 10, ingredient_type)
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock)
        receipt = burger.get_receipt()
        assert expected_prefix in receipt


class TestBurgerIntegration:
    """Интеграционные сценарии: несколько методов вместе."""

    def test_full_burger_assembly(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        burger.remove_ingredient(0)

        assert burger.bun == mock_bun
        assert burger.ingredients == [mock_sauce]
        assert burger.get_price() == BUN_PRICE_1 * 2 + SAUCE_PRICE

    def test_burger_receipt_after_modifications(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        receipt = burger.get_receipt()
        assert SAUCE_NAME not in receipt
        assert FILLING_NAME in receipt

    def test_burger_state_after_full_clear(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
        assert burger.get_price() == BUN_PRICE_1 * 2