def get_two_last_digits(number: int) -> tuple:
    return number // 10 % 10, number % 10


print(get_two_last_digits.__annotations__)
