class B:
    n = 5
    def adder(self, v):
        return v + self.n

w = B()
w.__dict__

w.n = 8
w.__dict__
