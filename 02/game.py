#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH, _load_words
import random
import itertools

NUM_LETTERS = 7

def draw_letters():
    return random.sample(POUCH, k=NUM_LETTERS)

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

            
   
def _get_permutations_draw(draw):
    permutations = []
    for i in range(0, NUM_LETTERS+1):
        p = list(itertools.permutations(draw, i))
        permutations += p
    return permutations
    
def get_possible_dict_words(permutations):
    possible_words = [x for x in permutations if ''.join(x).lower() in DICTIONARY]
    return possible_words

def check_top_score(score):
    with open('high_score.txt') as file:
        top_score = file.read()
        if score > int(top_score):
            print('New high score! {}'.format(score))
            with open('high_score.txt','w') as file:
                file.write((str(score)))

def main():
    draw = draw_letters()
    print('Letters drawn : {}'.format(draw))
    user_word = input('Make a word: \n')
    user_score = calc_word_value(user_word)
    print('User score for {} : {}'.format(user_word,user_score))
    assert set(user_word.upper()) < set(draw)
    assert user_word.lower() in DICTIONARY
    
    perms = _get_permutations_draw(draw)
    possible_words = get_possible_dict_words(perms)
    max_word = max_word_value(possible_words)
    max_score = calc_word_value(max_word)
    print('Top scoring word : {}, scoring {} points'.format(''.join(max_word),max_score))
    print('User score: {}'.format(user_score/max_score*100))
    check_top_score(user_score)

if __name__ == "__main__":
    main()
