import sys

str_text = [line.strip() for line in sys.stdin]
true_str = [i for i in str_text if i[0] == '#']

print(len(true_str))