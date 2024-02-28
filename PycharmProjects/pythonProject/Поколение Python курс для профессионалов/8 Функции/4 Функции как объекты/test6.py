def add_name(name, names=[]):
    names.append(name)


add_name('Timur')
add_name('Arthur')
add_name('Dima')
print(*add_name.__defaults__)
print(add_name.__class__)
