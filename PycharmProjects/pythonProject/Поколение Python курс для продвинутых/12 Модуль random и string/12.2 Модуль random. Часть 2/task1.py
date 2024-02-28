import random
def generate_ip():
    n = []
    for _ in range(4):
        n.append(str(random.randint(0, 255)))
    return ".".join(n)




