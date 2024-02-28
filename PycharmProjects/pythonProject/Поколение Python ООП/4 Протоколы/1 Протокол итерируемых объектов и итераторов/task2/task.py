class DevelopmentTeam:
    def __init__(self):
        self.juniors = tuple()
        self.seniors = tuple()

    def add_junior(self, *args):
        self.juniors += args

    def add_senior(self, *args):
        self.seniors += args

    def __iter__(self):
        yield from map(lambda x: (x, 'junior'), self.juniors)
        yield from map(lambda x: (x, 'senior'), self.seniors)


pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))