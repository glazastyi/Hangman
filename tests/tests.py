""" Tests for Hangman """

from Hangman import Hangman


def test_1(self):
    """
        Win
    """
    word = "Nikita"
    game = Hangman(word, 5)
    for letter in word:
        game.attempt(letter)
    game.check_status()
    self.assertEqual(game.status, 1)


def test_2(self):
    """
        The game is not over
    """
    word = "Nikita"
    game = Hangman(word, 5)
    for letter in word[:-1]:
        game.attempt(letter)
    game.check_status()
    self.assertEqual(game.status, 0)


def test_3(self):
    """
        Lost
    """
    word = "Nikita"
    game = Hangman(word, 5)
    for letter in word:
        print letter
        game.attempt("a")
    game.check_status()
    self.assertEqual(game.status, -1)
