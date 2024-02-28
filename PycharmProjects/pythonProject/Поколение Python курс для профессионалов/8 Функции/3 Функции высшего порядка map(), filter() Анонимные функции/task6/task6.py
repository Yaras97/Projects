def verification(login, password, success, failure):
    # Переменные для проверки условий
    has_letter = any(c.isalpha() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() and c.isascii() for c in password)
    has_digit = any(c.isdigit() for c in password)

    # Проверка условий
    if has_letter and has_upper and has_lower and has_digit:
        success(login)
    else:
        # Список ошибок с приоритетами
        errors = [
            ("в пароле нет ни одной буквы", not has_letter),
            ("в пароле нет ни одной заглавной буквы", not has_upper),
            ("в пароле нет ни одной строчной буквы", not has_lower),
            ("в пароле нет ни одной цифры", not has_digit)
        ]

        # Выбор строки-сообщения об ошибке с наивысшим приоритетом
        error_message = next((error for error, condition in errors if condition), None)

        failure(login, error_message)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)