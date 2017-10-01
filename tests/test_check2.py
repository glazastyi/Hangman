from Hangman import Hangman


def test_check2():
    word = "Hello"
    attempts = 5
    game = Hangman(word, attempts)
    for elem in word:
        game.attempt(elem)
    game.check_status()
    assert game.status == 1
