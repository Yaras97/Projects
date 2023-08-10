# put your python code here
a = input()
b = input()
c = input()
if min (len(a), len(b), len(c)) == len(a):
    print(a)
elif min (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max (len(a), len(b), len(c)) == len(a):
    print(a)
elif max (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)