n = input()
pol1 = len(n) // 2 + 1
pol2 = len(n) // 2
if len(n) % 2 == 0:
    print(n[pol2:], n[:pol2], sep='')
if len(n) % 2 == 1:
    print(n[pol1:], n[:pol1], sep='')
