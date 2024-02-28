num = [1, '2', 3, 4, 'five']
print(sum(list(filter(lambda x: isinstance(x, (int, float)), num))))