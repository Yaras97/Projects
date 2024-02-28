class HtmlTag:
    level = 0
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        if not self.inline:
            print(f"{'  ' * HtmlTag.level}<{self.tag}>")
            HtmlTag.level+=1
        else:
            print(f"{'  ' * HtmlTag.level}<{self.tag}>",end='')
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        if not self.inline:
            HtmlTag.level -= 1
            print(f"{'  ' * HtmlTag.level}</{self.tag}>")


    def print(self, text):
        if self.inline :
            print(f'{text}</{self.tag}>')
        else:
            print('  ' * HtmlTag.level + text)


with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')