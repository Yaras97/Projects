from datetime import date

class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except ValueError:
                raise TypeError("Аргумент переданного типа не поддерживается")
        elif isinstance(birth_date, (list, tuple)) and len(birth_date) == 3:
            try:
                self.birth_date = date(*birth_date)
            except ValueError:
                raise TypeError("Аргумент переданного типа не поддерживается")
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        return self.current_age(self.birth_date, today)

    @staticmethod
    def current_age(birth_date, today):
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age