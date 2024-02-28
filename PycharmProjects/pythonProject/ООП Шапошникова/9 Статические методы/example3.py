class A:
    @staticmethod
    def meth():
        print('meth')

a = A()
print(a.meth())
print(A.meth())

class B:
    @staticmethod
    def meth(value):
        print(value)

b = B()
print(b.meth(1))
print(B.meth('hello'))