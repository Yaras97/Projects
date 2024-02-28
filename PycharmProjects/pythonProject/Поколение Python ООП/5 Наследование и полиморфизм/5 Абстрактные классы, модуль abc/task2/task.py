from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self):
        pass


class King(ChessPiece):
    def can_move(self, hor, vert):
        shift = [abs(ord(self.horizontal) - ord(hor)), abs(self.vertical - vert)]
        return [False, True][max(shift) < 2 and sum(shift) > 0]


class Knight(ChessPiece):
    def can_move(self, hor, vert):
        shift = [abs(ord(self.horizontal) - ord(hor)), abs(self.vertical - vert)]
        return [False, True][max(shift) == 2 and min(shift) == 1]