"""Hangman game"""


class Hangman(object):
    """Hangman game"""

    def __init__(self, word, attempts_number):

        self.word = list(word)
        self.attempts_number = int(attempts_number)
        self.number_of_mistakes = 0
        self.guessed_word = ["*"] * len(word)
        self.status = 0

    def attempt(self, letter):
        if letter in self.word:
            index = self.word.index(letter)
            self.word[index] = "*"
            self.guessed_word[index] = letter
            print "Hit\n"
        else:
            self.number_of_mistakes += 1
            nom = self.number_of_mistakes
            attnum = self.attempts_number
            print "Missed, mistake %s out of %s.\n" % (nom, attnum)

    def check_status(self):
        if "*" not in self.guessed_word:
            print "The word: %s\n" % ("".join(self.guessed_word))
            print "You Win!\n"
            self.status = 1
        if self.number_of_mistakes >= self.attempts_number:
            print "You lost :("
            self.status = -1


def game(word, attempts_number, checker):
    play = Hangman(word, attempts_number)
    print "Start game\n"
    count = 0
    while play.status == 0 and count < len(word):
        letter = checker[count]
        play.attempt(letter)
        play.check_status()
        count += 1
    return play.status


if __name__ == "__main__":
    game("hello", 5, "Hello")
