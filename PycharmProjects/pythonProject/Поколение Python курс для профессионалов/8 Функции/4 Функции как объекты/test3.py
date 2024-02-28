def bee():
    return 'bee'


def geek():
    return 'geek'


bee, geek = geek, bee
print(bee())
print(geek())
