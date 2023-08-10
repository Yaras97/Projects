import random
let = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
def generate_password(length):
    pas = ''
    for i in range(m):
        pas += random.choice(let)
    return pas
def generate_passwords(count, length):
    lst = []
    for i in range(n):
        lst.append(generate_password(length))
    return lst

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')