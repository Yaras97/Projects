class Letters:
    def __init__(self, string):
        self.letters = []
        for i in string:
            self.letters.append(f'-{i}-')

    def __iter__(self):
        return iter(self.letters)
        # return LettersIterator(self.letters[:])
# 
# class LetterIterator:
#     def __init__(self, letters):
#         self.letters = letters
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.letter == []:
#             raise StopIteration
#         item = self.letter[0]
#         del self.letters[0]
#         return item


kit = Letters('worlds')
print(kit.letters)

for i in kit:
    print(i)

print(kit.letters)