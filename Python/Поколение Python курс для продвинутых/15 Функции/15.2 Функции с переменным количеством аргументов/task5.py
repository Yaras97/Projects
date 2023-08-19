def print_products(*args):
    if str() in args:
        s = []
        for i in args:
            if type(i) == str:
                if len(i) != 0:
                    s.append(i)
        if len(s) == 0:
            return print('Нет продуктов')
        return [print(f'{str(j + 1)}) {s[j]}') for j in range(len(s))]
    else:
        return print('Нет продуктов')