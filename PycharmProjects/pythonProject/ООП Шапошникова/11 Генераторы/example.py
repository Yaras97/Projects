def starmaker(n):
    while n > 0:
        yield '*'
        n -= 1


print(type(starmaker))
s = starmaker(3)
print(type(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))