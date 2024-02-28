class HistoryDict:
    def __init__(self, data=None):
        self._data = data or {}
        self._history = {key: [value] for key, value in self._data.items()}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self._history.setdefault(key, []).append(value)

    def __iter__(self):
        yield from self._data

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def keys(self):
        return iter(self._data.keys())

    def values(self):
        return iter(self._data.values())

    def items(self):
        return iter(self._data.items())

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history


historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())