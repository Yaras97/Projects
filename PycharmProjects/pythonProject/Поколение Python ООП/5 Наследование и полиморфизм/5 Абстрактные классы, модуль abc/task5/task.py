from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self._data = []
        for arg in args:
            start, stop = (arg, arg) if isinstance(arg, int) else map(int, arg.split('-'))
            self._data.extend(range(start, stop + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __len__(self):
        return len(self._data)