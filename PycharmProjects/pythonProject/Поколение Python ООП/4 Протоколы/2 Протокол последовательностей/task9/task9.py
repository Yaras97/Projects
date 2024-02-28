class MutableString:
    def __init__(self, string=''):
        self._string = string

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __str__(self):
        return self._string

    def __repr__(self):
        return f"MutableString('{self._string}')"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        return iter(self._string)

    def __getitem__(self, index):
        return self._string[index]

    def __setitem__(self, index, value):
        self._string = self._string[:index] + value + self._string[index + 1:]

    def __delitem__(self, index):
        self._string = self._string[:index] + self._string[index + 1:]

    def __add__(self, other):
        return MutableString(self._string + other._string)

mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))