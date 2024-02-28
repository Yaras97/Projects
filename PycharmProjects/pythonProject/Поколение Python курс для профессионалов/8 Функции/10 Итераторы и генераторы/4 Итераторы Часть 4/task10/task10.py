class Alphabet:
    def __init__(self, language):
        self.language = language
        self.en = [chr(let) for let in range(ord('a'), ord('z') + 1)]
        self.ru = [chr(let) for let in range(ord('а'), ord('я') + 1)]
        self.index = -1
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.language == 'en':
            if self.index == len(self.en):
                self.index = 0
            return self.en[self.index]
        if self.language == 'ru':
            if self.index == len(self.ru):
                self.index = 0
            return self.ru[self.index]


en_alpha = Alphabet('en')

for _ in range(100):
    print(next(en_alpha))