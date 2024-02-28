# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем",
# который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
# Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран.
# У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.


import random


class unit:  # создаем родительский клас юнитов с атрибутами: номер и команда
    def __init__(self, n, team):
        self.n = n
        self.team = team


class heroes(unit):  # создаем клас героев и добавляем атрибут уровень
    def __init__(self, name, n, team, level=0):
        self.name = name
        self.level = level
        self.team = team

    def level_up(self, incr):  # создаем метод повышения уровня, который принимает аргумент "на сколько повышен уровень"
        self.level += incr


class soldier(unit):  # создаем клас солдата с методом следовать за героем
    def follow_heroes(self, heroes):
        print("\n" + "Для охраны своих владений герой {} выбрал опытного воина № {} и отправился с ним в поход.".format(
            heroes.name, self.n))


Tristan, Merlin = heroes("Tristan", 1, "red"), heroes("Merlin", 2, "green")  # создаем два объекта героя
red_team = []  # создаем
green_team = []  # две коменды
quantity = int(input("Количество воинов:")) + 1  # пользовательский ввод обозначает общее количество воинов
for i in range(1, quantity):  # создам воинов и распределяем между командами героев
    t = random.randint(0, 1)
    i = soldier(i, t)
    if i.team == 0:
        red_team.append(i)
        i.team = "red"
    else:
        green_team.append(i)
        i.team = "green"
if len(red_team) > len(green_team):  # определяем уровень героя в зависимости от того у кого больше солдат
    Tristan.level_up(1)
elif len(red_team) < len(green_team):
    Merlin.level_up(1)
if len(red_team) >= 10:
    Tristan.level_up(len(red_team) // 5)
if len(green_team) >= 10:
    Merlin.level_up(len(green_team) // 5)

# выводим на экран списки команд
print("В войске героя по имени", Tristan.name + ",", str(Tristan.level) + "-го уровня,", len(red_team),
      "знатных воинов!")
for i in red_team:
    print(i.n, i.team, end=", ")
print("\n" + "В войске героя по имени", Merlin.name + ",", str(Merlin.level) + "-го уровня,", len(green_team),
      "знатных воинов!")
for i in green_team:
    print(i.n, i.team, end=", ")
# выводим случайное имя героя и номер одного из солдат
who = random.randint(0, 1)
if who == 1:
    t = red_team
    h = Tristan
else:
    t = green_team
    h = Merlin
random.choice(t).follow_heroes(h)