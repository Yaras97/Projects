import json


def is_correct_json(string):
    try:
        json.load(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


print(is_correct_json('["beegeek", 1, 2, 3]'))