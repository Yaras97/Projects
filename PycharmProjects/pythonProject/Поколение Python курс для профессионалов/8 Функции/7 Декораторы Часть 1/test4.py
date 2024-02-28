def add_dollar_prefix(func):
    def wrapper():
        result = str(func())
        return '$' + result

    return wrapper


@add_dollar_prefix
def get_price(item):
    prices = {'comic book': 5, 'puzzle': 15}
    return prices[item]


print(get_price('comic book'))
