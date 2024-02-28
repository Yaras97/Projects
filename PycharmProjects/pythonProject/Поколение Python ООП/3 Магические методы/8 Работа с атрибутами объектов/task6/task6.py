class AttrsNumberObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.attrs_num = 0

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattribute__(self, name):
        if name == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, name)


person = AttrsNumberObject(name='Mark')

print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)