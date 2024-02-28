import timeit
mysetup = 'from math import sqrt'

mycode = '''
mylist = []
for i in range(100):
    mylist.append(sqrt(i))
'''
print(timeit.timeit(stmt=mycode,
              setup=mysetup,
              number=10000))