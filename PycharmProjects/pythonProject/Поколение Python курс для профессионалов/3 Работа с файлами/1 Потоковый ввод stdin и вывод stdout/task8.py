import sys
from datetime import datetime
input_text = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]

# print(input_text)
# print(sorted(input_text))
# print(sorted(input_text, reverse=True))

if input_text == sorted(input_text):
    print('ASC')
elif input_text == sorted(input_text, reverse=True):
    print('DESC')
else:
    print('MIX')
