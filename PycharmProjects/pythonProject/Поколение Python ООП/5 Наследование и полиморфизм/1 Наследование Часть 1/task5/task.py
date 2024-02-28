class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return

class NumberValidator(Validator):
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        if isinstance(self.obj, (int, float)):
            return True
        return False


instances = [12, 34.1, [1, 2, 3], {4, 5, 6}, (7, 8, 9), {1: 'one'}, 'this is string']

for instance in instances:
    validator = NumberValidator(instance)
    print(validator.is_valid())