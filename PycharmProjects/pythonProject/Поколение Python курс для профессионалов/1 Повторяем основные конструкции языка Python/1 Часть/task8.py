def index_of_nearest(numbers, number):
    if numbers:
        min_number = min(numbers, key=lambda x: abs(number - x))
        return numbers.index(min_number)
    return -1

