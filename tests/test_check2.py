from Hangman import Hangman


def test_check2():
    word = "Hello"
    attempts = 5
    game = Hangman(word, attempts)
    for el in word:
        game.attempt(el)
    game.check_status()
    assert game.status == 1
