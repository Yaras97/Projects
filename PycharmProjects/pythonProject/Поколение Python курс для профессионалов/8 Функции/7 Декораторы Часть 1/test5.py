def add_dollar_prefix(func):
    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))
        return '$' + result

    return wrapper


@add_dollar_prefix
def get_price(item):
    prices = {'comic book': 5, 'puzzle': 20}
    return prices[item]


print(get_price(item='puzzle'))
