class A:
    field1 = 1

    def make_str(self):
        print(self.field1)


class B(A):
    field2 = 2

    def make_str(self):
        print(self.field1, self.field2)


class C(A):
    field3 = 3

    def make_str(self):
        print(self.field1, self.field3)