''' Generate horoscopes '''
from nltk.grammar import Nonterminal
from nltk import CFG
import random
import re

grammar = CFG.fromstring(open('data/grammar.txt').read())

def get_sentence(start=None, depth=7):
    start = start if start else grammar.start()

    if isinstance(start, Nonterminal):
        productions = grammar.productions(start)
        if not depth:
            # time to break the cycle
            terminals = [p for p in productions if not isinstance(start, Nonterminal)]
            if len(terminals):
                production = terminals
        production = random.choice(productions)

        sentence = []
        for piece in production.rhs():
            sentence += get_sentence(start=piece, depth=depth-1)
        return sentence
    else:
        return [start]

def format(sentence):
    for index, word in enumerate(sentence):
        if word == 'a' and index + 1 < len(sentence) and re.match(r'^[aeiou]', sentence[index + 1]):
            sentence[index] = 'an'
    text = ' '.join(sentence)
    text = text.replace(' ,', ',')
    return text

