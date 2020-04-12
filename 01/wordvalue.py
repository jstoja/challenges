"""
    Calculate Word value with Scrabble rules
"""
from collections import namedtuple
from data import DICTIONARY, LETTER_SCORES

ScrabbleWord = namedtuple('ScrabbleWord', 'word value')

def load_words():
    """ Load words from file """
    words = []
    with open(DICTIONARY, 'r') as word_file:
        for line in word_file:
            words.append(line.strip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in tuple(word):
        try:
            score += int(LETTER_SCORES[letter.upper()])
        except KeyError:
            continue
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    best_word = ScrabbleWord('', 0)
    for word in words:
        test_word = ScrabbleWord(word, calc_word_value(word))
        if test_word.value > best_word.value:
            best_word = test_word

    return best_word.word

if __name__ == "__main__":
    pass # run unittests to validate
