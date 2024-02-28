class Wordplay:
    def __init__(self, words = []):
        self.words = words

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return list(filter(lambda x: set(x) <= set(args), self.words))

    def avoid(self, *args):
        return list(filter(lambda x: len(set(x) & set(args)) == 0, self.words))


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)