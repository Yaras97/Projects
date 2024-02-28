class B:
    n = 5
    def adder(self, v):
            return v + self.n

b = B()
print(b.adder(33))


a = B()
a.n = 9
print(a.adder(3))

print(B.adder(B, 200))

print(B.adder(a, 200))