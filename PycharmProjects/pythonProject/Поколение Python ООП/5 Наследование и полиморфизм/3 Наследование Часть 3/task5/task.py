class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(int(str(self) + str(abs(self)) * (n-1)))

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))


superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))