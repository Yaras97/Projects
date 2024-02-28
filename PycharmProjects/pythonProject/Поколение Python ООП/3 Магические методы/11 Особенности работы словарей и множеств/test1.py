class Key:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'Key({repr(self.data)})'
    def __hash__(self):
        print('Вызов метода __hash__()', self.data)
        return 1
    def __eq__(self, other):
        print('Вызов метода __eq__()', self.data, other.data)
        if isinstance(other, Key):
            return self.data == other.data
        return NotImplemented
data = {}
key = Key('one')
print(data.__dir__())
data[key] = 1
print(data)
data[key] = 'один'
print()
print(data)