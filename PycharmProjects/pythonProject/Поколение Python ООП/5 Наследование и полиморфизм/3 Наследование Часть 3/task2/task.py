class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())

s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))

