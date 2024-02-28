class RoundedInt(int):
    def __new__(cls, num, even=True, *args, **kwargs):
        if even:
            if num % 2 == 0:
                num = num
            if num % 2 == 1:
                num += 1
        else:
            if num % 2 == 0:
                num += 1
            if num % 2 == 1:
                num = num

        instance = super().__new__(cls, num)
        instance.even = even
        return instance

for digit in range(100):
    print(RoundedInt(digit, False))