def get_method_owner(cls, method):
    for i_class in cls.mro():
        result = i_class.__dict__.get(method)
        if result:
            return i_class
    return None


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(get_method_owner(D, 'method'))