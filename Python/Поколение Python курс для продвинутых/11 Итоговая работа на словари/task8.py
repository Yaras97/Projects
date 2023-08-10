result = {}
dict1 = {'W': 'write', 'R': 'read', 'X': 'execute'}

for _ in range(int(input())):
    n = input().split()
    result[n[0]] = [dict1[i] for i in n[1:]]

for _ in range(int(input())):
    n = input().split()
    if n[0] in result[n[1]]:
        print("OK")
    else:
        print('Access denied')