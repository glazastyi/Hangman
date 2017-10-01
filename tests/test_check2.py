from Hangman import Hangman


def test_check2():
    word = "Hello"
    attempts = 5
    game = Hangman(word, attempts)
    game.attempt("H")
    game.attempt("e")
    game.attempt("l")
    game.attempt("l")
    game.attempt("o")

    assert game.status == 1
