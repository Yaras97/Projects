from itertools import tee
iters = tee([1, 2, 3, 4], 4)
totals = map(lambda a, b, c, d: a + b + c + d, *iters)
print(next(totals))
print(next(totals))
print(next(totals))
print(next(totals))