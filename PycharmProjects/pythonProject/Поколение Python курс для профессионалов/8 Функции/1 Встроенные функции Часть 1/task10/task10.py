
def zip_longest(*args, fill=None):
    for lst in args:
        for _ in lst:
            if len(lst) < len(max(args, key=len)):
                lst.append(fill)
    return list(zip(*args))


data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'], [False, False, True, True]]
print(zip_longest(*data, fill='skip'))