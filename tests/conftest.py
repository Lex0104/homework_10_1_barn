import pytest

@pytest.fixture
def number_string():
    return [
        "Maestro 1596 83** **** 5199",
        "**9589",
        "MasterCard 7158 30** **** 6758",
        "**5560",
        "Visa Classic 6831 98** **** 7658",
        "Visa Platinum 8990 92** **** 5229",
        "Visa Gold 5999 41** **** 6353",
        "**4305",
    ]


@pytest.fixture
def old_data() :
    return [
        "11.07.2018",
        "03.07.2019",
        "30.06.2018",
    ]


@pytest.fixture
def user_card_number() :
    return [
        "7000 79** **** 6361",
        "7158 30** **** 6758",
        "6831 98** **** 7658",
        "8990 92** **** 5229",
        "5999 41** **** 6353",
    ]


@pytest.fixture
def account_number() :
    return [
        "**4305",
        "**9589",
        "**5560",
        "**4305",
    ]


def list_dict() :
    return [
        {"id" : 41428829, "state" : "EXECUTED", "date" : "2019-07-03T18:35:29.512364"},
        {"id" : 939719570, "state" : "EXECUTED", "date" : "2018-06-30T02:08:58.425572"},
    ]
