class Summator:
    def total(self, n):
        return sum(i for i in range(1, n + 1))


class SquareSummator(Summator):
    def total(self, n):
        return sum(i**2 for i in range(1, n + 1))


class QubeSummator(Summator):
    def total(self, n):
        return sum(i**3 for i in range(1, n + 1))


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return sum(i**self.m for i in range(1, n + 1))


for i in range(5, 50):
    summator = CustomSummator(i)
    print(summator.total(10))