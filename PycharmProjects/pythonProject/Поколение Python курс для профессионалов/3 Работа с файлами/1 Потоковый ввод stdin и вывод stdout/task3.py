import sys

lucky_num = [int(line) for line in sys.stdin]
if len(lucky_num) % 2 == 1:
    if lucky_num[-1] % 2 == 0:
        print('Анри')
    else:
        print('Дима')
elif len(lucky_num) % 2 == 0:
    if lucky_num[-1] % 2 == 1:
        print('Анри')
    else:
        print('Дима')
