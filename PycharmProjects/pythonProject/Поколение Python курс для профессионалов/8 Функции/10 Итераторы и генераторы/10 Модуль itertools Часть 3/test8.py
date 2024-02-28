from itertools import tee
iters = tee('beegeek')
print(type(iters), len(iters))