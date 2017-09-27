def hangman(word,attempts_number):
    success = 0
    word = [ el for el in word]
    guessed_word = ["*" for el in word]
    i = 0
    while(i <= attempts_number and success == 0):a
        letter = raw_input("Guess a letter:")
        if letter in word:
            index = word.index(letter)
            word[index] = "*"
            guessed_word[index] = letter
            print "Hit"
        else:
            i += 1
            print "Missed, mistake %s out of %s."%(i,attempts_number)

        if "*" not in guessed_word:
            success = 1
        print "The word: %s" % ("".join(guessed_word))
    if success:
        print "You Win!"
    else:
        print "You Lost!"


hangman("Hello",5)