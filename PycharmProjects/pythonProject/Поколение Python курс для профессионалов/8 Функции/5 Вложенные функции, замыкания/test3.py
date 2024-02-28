def outer_function(arg):
    num = 5
    name = 'Timur'
    numbers = [1, 2, 3]

    def inner_function():  # определяем вложенную функцию
        print(arg)
        print(num)
        print(numbers)

    return inner_function  # возвращаем вложенную функцию


inner = outer_function('python')
for var in inner.__closure__:
    print(var.cell_contents)
