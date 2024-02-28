def filter_anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]


def filter_anagrams(word, words):
    return(list(filter(lambda x: sorted(x) == sorted(word), words)))