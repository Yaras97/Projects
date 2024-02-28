class B:
    def __init__(self, string):
        self.items = []
        for i in string:
            self.items.append(f'-{i.upper()}-')

    def __str__(self):
        return str(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __setitem__(self, key, value):
        self.items[key] = f'-{value.upper()}-'


group = B('abcd')
group[2] = 'u'

print(group)
print(group[1])

group2 = list('abcd')
group2[2] = 'u'
print(group2)
print(group2[1])


