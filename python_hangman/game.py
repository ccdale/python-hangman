"""This is the game module for the python-hangman package.

TODO:
    DONE - pick a random phrase from a list of pre-generated phrases
    DONE - present that phrase to the player as a series of underscores
    DONE - allow the player to guess a letter and show where the guesses match the phrase
    DONE - detect whether the guess is correct or not
    DONE - count the number of guesses and correct guesses
    DONE - display to the user the number of guesses so far and the total number of guesses allowed
    DONE - decide if the game has been won or lost by checking whether the player has
    guessed correctly within the allotted number of guesses.
    DONE - test whether the player has guessed the whole phrase or not
    testing visual studio code


phrases?

"""

import random

from python_hangman import phrases


def generatePhrase():
    """Returns a random phrase from a list of well known phrases or sayings."""
    # phrases = [
    #     "The cow jumped over the moon",
    #     "an apple a day",
    #     "its nice to be nice",
    #     "tommorrow is another day",
    #     "but its tomorrow today",
    #     "such a sunny day"
    # ]
    return random.choice(phrases)


def hangmanHint(phrase, guesses):
    ret = "\n "
    underscores = 0
    for letter in phrase:
        if letter == " ":
            op = "  "
        else:
            if letter in guesses:
                op = f"{letter.upper()} "
            else:
                op = "_ "
                underscores += 1
        ret += op
    return ret, underscores

def askMe(phrase):
    ok = False
    while not ok:
        inp = input("guess a letter: ").lower()

        if len(inp) == 1:
            for letter in range(ord("a"), ord("z")+1):
                if inp == chr(letter):
                    ok = True
                    break
        elif len(inp) > 1:
            if inp == phrase:
                return True
        else:
            pass
    return inp

def testGuess(guess, phrase):
    if guess in phrase:
        return True
    return False


def hangman():
    """This is the hangman game from the python-hangman package."""
    numberofincorrectguesses = 0
    totalallowed = 10
    phrase = generatePhrase()
    guesses = []
    wongame = False
    while numberofincorrectguesses < totalallowed:
        guess = askMe(phrase)
        if type(guess) != str:
            if guess == True:
                wongame = True
                break
        elif testGuess(guess, phrase):
            guesses.append(guess)
            print(guesses)
        else:
            numberofincorrectguesses += 1
        hint, underscores = hangmanHint(phrase, guesses)
        if underscores == 0:
            wongame = True
            break
        print(f"{hint}\n{numberofincorrectguesses}/{totalallowed}")

    # if numberofincorrectguesses >= totalallowed:
    print(f"game over, {numberofincorrectguesses}/{totalallowed}\n{phrase}\n")
    msg = "game won" if wongame else "game lost"
    print(msg)
    return True


if __name__ == "__main__":
    hangman()
