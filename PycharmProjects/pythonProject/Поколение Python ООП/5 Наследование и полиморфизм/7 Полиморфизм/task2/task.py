from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=()):
        self._data = list(iterable)

    def add(self, obj):
        self._data.append(obj)

    def clear(self):
        self._data.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        if self._data:
            return min(self._data)
        return None


class MaxStat(Stat):
    def result(self):
        if self._data:
            return max(self._data)
        return None


class AverageStat(Stat):
    def result(self):
        if self._data:
            return sum(self._data) / len(self._data)
        return None