import sys

str_text = [line for line in sys.stdin]
true_text = []
for i in str_text:
    true_text.append(i.strip().split('/'))


txt = {}
for j in true_text:
    if len(j) > 1:

        if true_text[-1][0].strip() == j[1].strip():
            # txt[float(j[2].strip())] = j[0]
            txt.setdefault(j[2].strip(), []).append(j[0])


txt = dict(sorted(txt.items(), key=lambda x: x))

for key, item in txt.items():
    print(*sorted(item), sep='\n')
