class AnyClass:
    result = ()
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.result += (str(key) + '=' + "'" + str(value) + "'", )

    def __str__(self):
        return f'AnyClass: {", ".join(self.result)}'

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(self.result)})'


cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]