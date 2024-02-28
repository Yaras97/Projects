class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.paragraph = []

    def add(self, words):
        words_list = words.split()
        current_line = ''
        for word in words_list:
            if len(current_line) + len(word) + 1 <= self.length:
                current_line += word + ' '
            else:
                self.paragraph.append(current_line.strip())
                current_line = word + ' '
        if current_line:
            self.paragraph.append(current_line.strip())

    def end(self):
        for line in self.paragraph:
            print(line)
        self.paragraph = []


class RightParagraph:
    def __init__(self, length):
        self.length = length
        self.paragraph = []

    def add(self, words):
        words_list = words.split()
        current_line = ''
        for word in words_list:
            if len(current_line) + len(word) + 1 <= self.length:
                current_line += word + ' '
            else:
                self.paragraph.append(current_line.strip())
                current_line = word + ' '
        if current_line:
            self.paragraph.append(current_line.strip())

    def end(self):
        for line in self.paragraph:
            print(f"{(self.length - len(line)) * ' '}{line}")
        self.paragraph = []


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()