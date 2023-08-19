n = input()
count = 0
for i in n:
    if i == "f":
        count += 1
if count == 1:
    print(n.find("f"))
elif count > 1:
    print(n.find("f"),  n.rfind("f"))
else:
    print('NO')