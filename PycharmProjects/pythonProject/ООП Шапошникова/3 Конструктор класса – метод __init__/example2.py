class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qual = q

    def method(self):
        print(self.name, self.surname, self.qual)


    def __del__(self):
        print(f'До свидания {self.name} {self.surname}')



man1 = Person('Oleg', 'Dakarov')
man2 = Person('Misha', 'Polo')
man3 = Person('Zina', 'Coy')

