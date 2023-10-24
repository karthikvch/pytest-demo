import pytest

from shopping_cart import ShoppingCart


def test_can_add_items_to_cart():
    cart = ShoppingCart()
    pass


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    x = "1"
    assert x == "1"
