class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, number=1):
        self.value += number

    def dec(self, number=1):
        self.value -= number
        if self.value < 0:
            self.value = 0

class NonDecCounter(Counter):
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, number=1):
        self.value += number

    def dec(self, number=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.start = start
        self.limit = limit
        self.value = self.start

    def inc(self, number=1):
        if self.value + number > self.limit:
            self.value = self.limit
        else:
            self.value += number


digits = [46, 158, 79, 100, 161, 100, 30, 27, 132, 79, 152, 114, 97, 171, 71, 35, 186, 157, 149, 144, 156, 41, 172, 122,
          131, 141, 69, 113, 86, 46, 104, 147, 42, 60, 31, 32, 190, 107, 110, 103, 77, 135, 35, 33, 104, 191, 94, 55,
          50, 156]

counter = LimitedCounter(start=10, limit=2000)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)
