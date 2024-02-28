import string

print(string.printable)
for i in string.printable:
    print(hash(i) % 20)