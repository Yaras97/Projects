import random
import string


def generate_index():
    n = ""
    for i in range(7):
        if i == 3:
            n += '_'
        elif i == 2:
            n += str(random.randint(0, 99))
        elif i == 4:
            n += str(random.randint(0, 99))
        else:
            n += random.choice(string.ascii_uppercase)
    return n