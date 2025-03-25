"""This is where dictionary tests happens!"""

_author_ = "730678802"

from dictionary import invert
import pytest


def test_invert_use1() -> None:
    """Test the invert function"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_use2() -> None:
    """Test the invert function"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_edge() -> None:
    """Test the invert function"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)
