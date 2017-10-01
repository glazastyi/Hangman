from Hangman import Hangman


def test_check():
    word = "Hello"
    attempts = 5
    game = Hangman(word, attempts)
    assert game.word == list(word)
    assert game.attempts_number == int(attempts)
    assert game.number_of_mistakes == 0
    assert game.guessed_word == ["*"] * len(word)
    assert game.status == 0
