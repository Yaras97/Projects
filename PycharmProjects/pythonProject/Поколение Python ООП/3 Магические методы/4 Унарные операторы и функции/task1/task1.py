class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])


string = ReversibleString("Namespaces are one honking great idea -- let's do more of those!")

print(string)
print(-string)