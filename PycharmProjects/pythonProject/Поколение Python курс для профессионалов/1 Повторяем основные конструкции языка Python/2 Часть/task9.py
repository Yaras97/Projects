d = {}
d_units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
d_units_trans = {1: 'B', 2: 'KB', 3: 'MB', 4: 'GB'}

def converter(x):
    s = 1024
    for i in range(1, 5):
        if x > s:
            x /= s
        else:
            break
    return str(round(x)), d_units_trans[i]

with open('files.txt', encoding='utf-8') as file:
    for line in file:
        name_full, size, unit = line.split()
        name, f_ext = name_full.split('.')
        d.setdefault(f_ext, []).append((name, int(size) * d_units[unit]))
    for k in sorted(d):
        total = 0
        for i in sorted(d[k]):
            print(i[0] + '.' + k)
            total += i[1]
        print('---------')
        print('Summury:', *converter(total))
        print()
        