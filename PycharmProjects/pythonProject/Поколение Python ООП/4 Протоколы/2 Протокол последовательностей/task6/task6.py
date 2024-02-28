class AttrDict:
    def __init__(self, data=dict()):
        self._data = dict(data)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getattr__(self, attr):
        return self._data[attr]

    def __setattr__(self, attr, value):
        if attr == '_data':
            super().__setattr__(attr, value)
        else:
            self._data[attr] = value

attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)