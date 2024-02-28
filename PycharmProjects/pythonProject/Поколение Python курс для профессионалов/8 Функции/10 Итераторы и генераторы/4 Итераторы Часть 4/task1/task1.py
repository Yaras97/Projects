class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


repeater = Repeater(1234)

for _ in range(100):
    print(next(repeater))
