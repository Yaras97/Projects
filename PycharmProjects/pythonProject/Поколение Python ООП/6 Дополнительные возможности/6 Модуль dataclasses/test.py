from dataclasses import dataclass, field
@dataclass
class Person:
    name: str
    surname: str
    age: int = field(repr=True)
person = Person('Гвидо', 'ван Россум', 67)
print(person)
print(person.age)