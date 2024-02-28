from functools import partial
beegeek = partial(print, 'bee', 'geek', end='!')
print(beegeek.args)
print(beegeek.keywords)
