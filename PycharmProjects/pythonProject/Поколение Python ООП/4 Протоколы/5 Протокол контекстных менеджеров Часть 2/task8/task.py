from copy import copy, deepcopy

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy = deepcopy(self.data) if deep else copy(self.data)

    def __enter__(self):
        return self.copy

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is None:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.copy)
            else:
                self.data.update(self.copy)
        return True
