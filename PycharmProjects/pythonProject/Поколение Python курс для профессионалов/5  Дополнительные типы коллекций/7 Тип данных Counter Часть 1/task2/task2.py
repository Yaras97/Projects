from collections import Counter


def count_occurences(word, words):
    counter = Counter()
    counter.update(words.lower().split())
    return counter[word]


word = 'step'
words = 'stepik bEe Bee BEe STEP STEP bee STEP stepik stepik STEPik STEPIK'

print(count_occurences(word, words))