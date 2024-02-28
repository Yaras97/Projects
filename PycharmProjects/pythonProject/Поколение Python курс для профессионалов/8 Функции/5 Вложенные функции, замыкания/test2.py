def outer_function():
    num = 5
    def inner_function(): # определяем вложенную функцию
        num += 10
        print(num)


inner_function() # вызываем вложенную функцию
outer_function()