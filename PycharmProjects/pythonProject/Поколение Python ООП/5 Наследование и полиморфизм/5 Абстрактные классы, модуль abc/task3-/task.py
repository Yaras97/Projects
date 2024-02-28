from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self):
        self._attr = None

    @property
    def attr(self):
        if self._attr is None:
            raise AttributeError('Атрибут не найден')
        return self._attr

    @attr.setter
    def set_attr(self, attr):
        if self.validate(self._attr):
            self._attr = attr


    @abstractmethod
    def validate(self):
        pass