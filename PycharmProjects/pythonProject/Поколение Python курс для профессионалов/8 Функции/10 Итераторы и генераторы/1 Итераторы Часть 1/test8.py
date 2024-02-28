beegeek = 'beegeek'
iter1 = iter(beegeek)
iter2 = iter(beegeek)
iter3 = iter(beegeek)
next(iter2)
next(iter3)
next(iter3)
print(next(iter1) + next(iter2) + next(iter3))