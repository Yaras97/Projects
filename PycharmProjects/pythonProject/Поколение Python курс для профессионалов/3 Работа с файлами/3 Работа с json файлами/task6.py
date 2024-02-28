import json
import sys

input_text = str()
for i in sys.stdin:
    input_text += i.strip()
json_form = json.loads(input_text)
for key, item in json_form.items():
    if type(item) is list:

        print(f'{key}: {", ".join(item)}')
    else:
        print(f'{key}: {item}')
