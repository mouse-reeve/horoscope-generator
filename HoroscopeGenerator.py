''' Generate horoscopes '''
from nltk.grammar import Nonterminal
from nltk import CFG
import random

grammar = CFG.fromstring(open('grammar.txt').read())

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

for i in range(10):
    print ' '.join(get_sentence(depth=10))
