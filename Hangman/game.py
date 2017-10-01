from Hangman import Hangman


def game(word, attempts_number):
    play = Hangman(word, attempts_number)
    count = 0
    while play.status == 0:
        letter = raw_input("Guess a letter: ")
        play.attempt(letter)
        play.check_status()
        count += 1
    return play.status


if __name__ == "__main__":
    game(raw_input("Enter the word for the game: "), 5)
