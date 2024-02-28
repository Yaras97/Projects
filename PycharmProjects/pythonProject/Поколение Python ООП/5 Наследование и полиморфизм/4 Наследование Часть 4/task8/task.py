from collections import UserString

class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.data))
            self.data = self.data[:start] + str(value) + self.data[stop:]
        else:
            if index < 0:
                index += len(self.data)
            self.data = self.data[:index] + str(value) + self.data[index+1:]

    def __delitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.data))
            self.data = self.data[:start] + self.data[stop:]
        else:
            if index < 0:
                index += len(self.data)
            self.data = self.data[:index] + self.data[index+1:]



mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)