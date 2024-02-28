from collections import Counter


def scrabble(symbols, word):
    sym_count = Counter(symbols.lower())
    word_count = Counter(word.lower())
    sym_count.subtract(word_count)
    negative_number = list(filter(lambda x: x < 0, sym_count.values()))
    if negative_number:
        return False
    else:
        return True



print(scrabble('b1e2e3g4e___e___k', 'BeegeeK'))