class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        # instance.content = content
        return instance

    def title(self):
        return self.text_title

    # def __str__(self):
    #     return self.content

titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)