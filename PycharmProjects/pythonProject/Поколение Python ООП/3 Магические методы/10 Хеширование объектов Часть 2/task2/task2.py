class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def _fields(self):
        return tuple(self.__dict__.items())

    def __repr__(self):
        attrs = ', '.join(f'{name}={repr(value)}' for name, value in self._fields)
        return f'Row({attrs})'

    def __eq__(self, other):
        if isinstance(other, Row):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')
