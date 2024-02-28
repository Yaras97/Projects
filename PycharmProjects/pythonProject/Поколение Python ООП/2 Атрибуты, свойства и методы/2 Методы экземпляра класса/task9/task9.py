class Numbers:
    def __init__(self):
        self.nums = []

    def add_number(self, num):
        self.nums.append(num)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.nums))

    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.nums))


numbers = Numbers()

for n in range(0, 100, 2):
    numbers.add_number(n)

print(numbers.get_even())
print(numbers.get_odd())