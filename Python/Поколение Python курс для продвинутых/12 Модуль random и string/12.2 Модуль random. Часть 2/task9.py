import random
st = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
let = 'abcdefghijkmnpqrstuvwxyz'
letup = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
dig = '23456789'

def generate_password(length):
    pas = ''
    pas += random.choice(let)
    pas += random.choice(letup)
    pas += random.choice(dig)
    for i in range(m - len(pas)):
        pas += random.choice(st)
    a = list(pas)
    random.shuffle(a)
    a = ''.join(a)
    return a
def generate_passwords(count, length):
    lst = []
    for i in range(n):
        lst.append(generate_password(length))
    return lst

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')