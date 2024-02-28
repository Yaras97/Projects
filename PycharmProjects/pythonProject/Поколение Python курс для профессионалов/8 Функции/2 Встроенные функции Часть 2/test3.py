def bee():
    return 'bee'


def geek():
    return 'geek'


code = '''li = [bee() + geek() for _ in range(2)]
print(li)'''
exec(code)