def choose_plural(n, words):
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} {words[0]}'
    elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return f'{n} {words[1]}'
    else:
        return f'{n} {words[2]}'



# def choose_plural(amount, variants):
#     variant = 2
#     if amount % 10 == 1 and amount % 100 != 11:
#         variant = 0
#     elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
#         variant = 1
#     return '{} {}'.format(amount, variants[variant])



# def choose_plural(amount: int, declensions: tuple):
#     if str(amount).endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
#         return f'{amount} {declensions[2]}'
#     elif str(amount).endswith('1'):
#         return f'{amount} {declensions[0]}'
#     else:
#         return f'{amount} {declensions[1]}'