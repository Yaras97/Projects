import sys
progress = [int(line) for line in sys.stdin]

d_ar = []
for i in range(len(progress) - 1):
    d_ar.append(progress[i + 1] - progress[i])

d_geo = []
for i in range(len(progress) - 1):
    d_geo.append(progress[i + 1] / progress[i])

if all(map(lambda x: True if d_ar[0] == x else False, d_ar)):
    print('Арифметическая прогрессия')
if all(map(lambda x: True if d_geo[0] == x else False, d_geo)):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')