import re


class CaseHelper:
    CAMEL_CASE = re.compile(r'^([A-Z][a-z]+)+$')
    SNAKE_CASE = re.compile(r'^([a-z]+_?)+$')

    @staticmethod
    def is_snake(string):
        return bool(CaseHelper.SNAKE_CASE.search(string))

    @staticmethod
    def is_upper_camel(string):
        return bool(CaseHelper.CAMEL_CASE.search(string))

    @staticmethod
    def to_snake(string):
        string = re.sub(r'\B([A-Z])\B', r'_\1', string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())