def print_fio(name, surname, patronymic):
    print(*[surname.upper()[0], name.upper()[0], patronymic.upper()[0]], sep="")


name, surname, patronymic = input(), input(), input()


print_fio(name, surname, patronymic)