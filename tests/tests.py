from Hangman import Hangman


def test_check():
    word = "Hello"
    attempts = 5
    game = Hangman(word,attempts)
    assert  game.word == word
