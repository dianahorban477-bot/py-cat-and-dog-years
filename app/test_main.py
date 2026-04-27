from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_15_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_24_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_28_cat_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_14_years():
    assert get_human_age(14, 14) == [0, 0]


def test_23_years():
    assert get_human_age(23, 23) == [1, 1]


def test_27_years():
    assert get_human_age(27, 27) == [2, 2]


def test_100_years():
    assert get_human_age(100, 100) == [21, 17]
