from collections import Counter

text = Counter(input().lower().split())
min_value = text.most_common()[-1][1]
new_list = []
for key in sorted(text):
    if text[key] == min_value:
        new_list.append(key)

print(*new_list, sep=', ')