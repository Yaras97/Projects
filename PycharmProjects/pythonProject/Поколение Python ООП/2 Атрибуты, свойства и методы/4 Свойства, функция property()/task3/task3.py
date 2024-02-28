class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name_surname(self):
        return self.name + ' ' + self.surname

    def set_name_surname(self, name_surname):
        self.name, self.surname = name_surname.split()

    fullname = property(get_name_surname, set_name_surname)

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)