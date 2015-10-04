''' Generate horoscopes '''
import logging
from nltk.grammar import Nonterminal
from nltk import CFG
from os import path
import random
import re

HERE = path.abspath(path.dirname(__file__))

try:
    GRAMMAR = CFG.fromstring(open('%s/data/grammar.txt' % HERE).read())
except IOError:
    logging.error('Unable to load grammar file')
    raise IOError

def get_sentence(start=None, depth=7):
    ''' follow the grammatical patterns to generate a random sentence '''
    if not GRAMMAR:
        return 'Please set a GRAMMAR file'

    start = start if start else GRAMMAR.start()

    if isinstance(start, Nonterminal):
        productions = GRAMMAR.productions(start)
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

def format_sentence(sentence):
    ''' fix display formatting of a sentence array '''
    for index, word in enumerate(sentence):
        if word == 'a' and index + 1 < len(sentence) and re.match(r'^[aeiou]', sentence[index + 1]):
            sentence[index] = 'an'
    text = ' '.join(sentence)
    text = text.replace(' ,', ',')
    return text
