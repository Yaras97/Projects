def process_number(n, original_n):
    # Выводим текущее число
    print(f'n = {n}')

    # Базовый случай: если число стало неположительным или если n стало равным original_n, завершаем рекурсию
    if n <= 0 or n == original_n:
        return

    # Рекурсивный случай: вычитаем 5 и вызываем функцию снова
    process_number(n - 5, original_n)

    # Выводим промежуточный результат
    print(f'n − 5 = {n - 5}')


# Вводим число
number = int(input("Введите натуральное число: "))
# Вызываем функцию для обработки числа с вычитанием 5
process_number(number - 5, number)