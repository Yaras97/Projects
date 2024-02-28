class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, C, D):
    pass


class F(B, C):
    pass


print(MROHelper.len(E))
print(MROHelper.class_by_index(E, 4))
print(MROHelper.index_by_class(E, C))