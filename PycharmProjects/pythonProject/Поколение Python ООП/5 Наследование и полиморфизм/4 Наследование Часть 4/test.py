class UpperCaseDict(dict):
    def __init__(self, items=(), **kwargs):
        self.update(items)
        self.update(kwargs)

    def update(self, items):
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            self[key] = value

    def __setitem__(self, key, value):
        key = str(key).upper()
        print(key)
        super().__setitem__(key, value)

    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'


numbers = UpperCaseDict(one=1, two=2, three=3)
print(numbers)


