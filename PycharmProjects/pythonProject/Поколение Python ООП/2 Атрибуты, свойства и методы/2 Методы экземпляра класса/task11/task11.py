class Todo:
    def __init__(self):
        self.things = []

    def add(self, do, priority):
        self.things.append((do, priority))

    def get_by_priority(self, n):
        try:
            return list(map(lambda x: x[0], filter(lambda x: x[1] == n, self.things)))
        except:
            return []

    def get_low_priority(self):
        try:
            self.low = min(self.things, key=lambda x: x[1])[1]
            return list(map(lambda x: x[0], filter(lambda x: x[1] == self.low, self.things)))
        except:
            return []
    def get_high_priority(self):
        try:
            self.high = max(self.things, key=lambda x: x[1])[1]
            return list(map(lambda x: x[0], filter(lambda x: x[1] == self.high, self.things)))
        except:
            return []

todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())