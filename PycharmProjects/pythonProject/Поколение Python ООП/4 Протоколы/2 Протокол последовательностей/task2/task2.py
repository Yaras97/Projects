class SparseArray:
    def __init__(self, default):
        self.sequence = []
        self.default = default

    def __len__(self):
        return len(self.sequence)

    def __setitem__(self, key, value):
        if key >= self.__len__():
            self.sequence += [self.default] * (key + 1)
        self.sequence[key] = value

    def __getitem__(self, key):
        if key >= self.__len__():
            return self.default
        return self.sequence[key]


array = SparseArray('Тут ничего нет')

array[1000] = 1000
print(array[999])
print(array[1000])