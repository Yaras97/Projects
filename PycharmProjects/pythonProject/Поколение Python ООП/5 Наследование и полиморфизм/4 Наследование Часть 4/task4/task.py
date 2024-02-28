class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(str(item) for item in self)

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:] = list(filter(func, self))


advancedlist = AdvancedList(['hello', 'Gvido', 'how', 'are', 'you'])
advancedlist.map(len)
print(advancedlist)