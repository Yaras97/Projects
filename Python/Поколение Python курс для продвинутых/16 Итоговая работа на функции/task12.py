def gematria(word):
    return sum(map(lambda x: ord(x.upper()) - 65, word)), word

words = [input() for _ in range(int(input()))]

print(*sorted(words, key=gematria), sep='\n')
