def add(**kwargs):
    print(kwargs)
    print(*kwargs)
    print(type(kwargs))


kw = dict(attr1='bee', attr2='geek')

add.__dict__['attr1'] = 'bee'
add.__dict__['attr2'] = 'geek'
add(**kw)
print(add.attr1)