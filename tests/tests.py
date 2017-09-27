""" Tests for Hangman """
from Hangman import game


def test_1():
    """
        Win
    """
    assert game("hello", 5, "hello") == 1


def test_2():
    """
        The game is not over
    """
    assert game("hello", 5, "Hello") == 0


def test_3():
    """
        Lost
    """
    assert game("hello", 5, "AAAAA") == -1
