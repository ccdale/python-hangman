"""This is the game module for the python-hangman package.

TODO:
    pick a random phrase from a list of pre-generated phrases
    present that phrase to the player as a series of underscores
    allow the player to guess a letter and show where the guesses match the phrase
    count the number of guesses
    decide if the game has been won or lost by checking whether the player has
    guessed correctly within the allotted number of guesses.
    display to the user the number of guesses so far and the total number of guesses allowed


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
    #     "such a sunny day",
    # ]
    return random.choice(phrases)


def hangman():
    """This is the hangman game from the python-hangman package."""
    phrase = generatePhrase()
    print(phrase)
    return True


if __name__ == "__main__":
    hangman()
