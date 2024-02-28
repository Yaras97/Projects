n = input().split('-')
if ''.join(n).isdigit():
    if (n[0] == "7" and len(n[1]) == 3 and len(n[2]) == 3 and len(n[3]) == 4) or (len(n[0]) == 3 and len(n[1]) == 3 and len(n[2]) == 4):
        print('YES')
    else:
        print('NO')
else:
    print('NO')