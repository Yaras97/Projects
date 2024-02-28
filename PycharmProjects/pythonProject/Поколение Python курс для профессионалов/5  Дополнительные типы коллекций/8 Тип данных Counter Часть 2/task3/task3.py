from collections import Counter

text = Counter(input().lower().split())
sorted_values = sorted(text.most_common(), key=lambda x: (x[1], x[0]), reverse=True)
print(sorted_values[0][0])

