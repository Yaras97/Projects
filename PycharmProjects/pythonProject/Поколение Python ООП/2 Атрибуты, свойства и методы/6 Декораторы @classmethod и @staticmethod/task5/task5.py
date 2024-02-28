class StrExtension:
    @staticmethod
    def remove_vowels(string):
        vowels = 'aeiou'
        return ''.join(list(filter(lambda x: x.lower() not in vowels, string)))

    @staticmethod
    def leave_alpha(string):
        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        return ''.join(list(filter(lambda x: x.lower() in letters, string)))

    @staticmethod
    def replace_all(string, chars, char):
        return ''.join(list(map(lambda x: char if x in chars else x, string)))

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))