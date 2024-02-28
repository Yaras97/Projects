def nop(*rest, **kwargs):
    pass # заглушка, функция ничего не делает


print = nop
print('Привет', 'мир')
print('Stepik', 'Beegeek', 'Python', sep='*', end='')
print('Stepik', 'Beegeek', 'Python', delimeter='-', endline='\n')