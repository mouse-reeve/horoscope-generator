''' Generate horoscopes '''
from nltk.parse.generate import generate
from nltk import CFG
import random

grammar = CFG.fromstring(open('grammar.txt').read())

sentences = []
for sentence in generate(grammar, depth=5):
    sentences.append(' '.join(sentence))

for i in range(25):
    print(random.choice(sentences))
