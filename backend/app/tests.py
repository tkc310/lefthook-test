from .models import *  # noqa: F403 F401


def square(a: int, b: int) -> list:
    return a * b


def test_case():
    assert square(2, 3) == 6
