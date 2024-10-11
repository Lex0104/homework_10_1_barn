import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "user_card_number, new_string", [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ]
)
def test_get_mask_card_number(user_card_number, new_string):
    assert get_mask_card_number(user_card_number) == new_string


@pytest.mark.parametrize (
    "account_number, new_mask",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_number, new_mask):
    assert get_mask_account(account_number) == new_mask
