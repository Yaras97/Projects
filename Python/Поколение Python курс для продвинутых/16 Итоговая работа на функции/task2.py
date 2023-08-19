def pretty_print(data, side='-', delimiter='|'):
    s = f' {delimiter} '.join(map(str, data))
    print('', (len(s) + 2) * side)
    print(delimiter, s, delimiter)
    print('', (len(s) + 2) * side)