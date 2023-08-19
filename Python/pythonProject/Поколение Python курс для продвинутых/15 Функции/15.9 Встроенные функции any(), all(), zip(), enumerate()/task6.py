s = input()
digits = any(map(lambda char: char.isdigit(), s))
small = any(map(lambda cha: cha.isalpha() and cha == cha.lower(), s))
big = any(map(lambda ch: ch.isalpha() and ch == ch.upper(), s))
dl = len(s)

print('YES' if all((digits, small, big, dl >= 7)) else 'NO')