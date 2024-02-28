from functools import total_ordering


@total_ordering
class RomanNumeral:
    d = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
         "IV": 4, "I": 1}

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        total = 0
        prev_num, cur_num = 0, 0
        for c in self.number:
            cur_num = self.__class__.d[c]
            total -= prev_num if prev_num < cur_num else -prev_num
            prev_num = cur_num
        return total + cur_num

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented

    @classmethod
    def from_int(cls, number):
        keys = list(cls.d.keys())
        idx, res = 0, ""
        while number > 0:
            if number // cls.d[keys[idx]]:
                number -= cls.d[keys[idx]]
                res += keys[idx]
            else:
                idx += 1
        return cls(res)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.from_int(int(self) + int(other))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.from_int(int(self) - int(other))
        return NotImplemented

number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))