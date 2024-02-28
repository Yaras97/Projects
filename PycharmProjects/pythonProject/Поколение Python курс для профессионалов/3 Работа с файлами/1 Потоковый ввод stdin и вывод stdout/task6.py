import sys

str_text = [line for line in sys.stdin]
true_text = []
for i in str_text:
    if i.strip().startswith('#') == False:
        true_text.append(i)


print(*true_text)
