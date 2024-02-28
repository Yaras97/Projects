def bee():
    yield from 'bee'


def geek():
    yield from 'geek'


def beegeek():
    yield from bee()
    yield from geek()


print(list(beegeek()))
print(list(bee()))
print(*beegeek())