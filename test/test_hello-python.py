import pytest
from src.hello_python.hello_python import get_game_date


def test_get_game_date():
    raw_date = "56-2019-05-18"
    assert get_game_date(raw_date) == {"year": "2019", "month": "05", "day": "18"}


def test_bad_get_game_date():
    raw_date = "56-2019-05-21"
    assert not get_game_date(raw_date) == {"year": "2019", "month": "05", "day": "18"}
