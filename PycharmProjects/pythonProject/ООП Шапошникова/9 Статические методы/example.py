class A:
    def meth(self):
        print('meth')


a = A()
print(a.meth())
print(A.meth(a))

b = 10
A.meth(b)
b.meth()