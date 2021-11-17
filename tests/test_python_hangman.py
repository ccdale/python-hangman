from python_hangman import __version__, phrases
from python_hangman.game import hangman, generatePhrase


def test_version():
    assert __version__ == "0.1.0"


def test_hangman():
    """This tests the hangman function returns True if the Game is won"""
    result = hangman()
    assert result == True


def test_generatePhrase():
    """this tests that the generatPhrase function returns a string of some length."""
    phrase = generatePhrase()
    assert type(phrase) == str
    assert len(phrase) > 0


def test_genphrase_actual():
    """This tests the complete phrase actually exists."""
    phrase = generatePhrase()
    assert phrase in phrases
