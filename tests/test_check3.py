from Hangman import Hangman


def test_check2():
    word = "Hello"
    attempts = 5
    game = Hangman(word, attempts)
    for el in word[:-1]:
        game.attempt(el)
    game.attempt("a")
    game.check_status()
    assert game.status == 0
    assert game.number_of_mistakes == 1
    game.attempt("a")
    assert game.number_of_mistakes == 2
    game.attempt("b")
    assert game.number_of_mistakes == 3
    game.attempt("c")
    assert game.number_of_mistakes == 4
    game.attempt("d")
    assert game.number_of_mistakes == 5
    game.check_status()
    assert game.status == -1
