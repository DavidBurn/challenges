from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        dic = file.read()
        dic = dic.strip().split()
    return dic

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = sum([LETTER_SCORES[letter.upper()] for letter in word])
    return value
    

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""  
    max_score = 0
    top_word = ''
    for word in words:
        try:
            value = sum([LETTER_SCORES[letter.upper()] for letter in word])
        except KeyError:
            word = word.replace('-','')
        if value > max_score:
            max_score = value
            top_word = word
    return top_word

if __name__ == "__main__":
    pass # run unittests to validate
