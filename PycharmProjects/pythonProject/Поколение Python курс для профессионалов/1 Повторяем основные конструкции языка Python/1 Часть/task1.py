def hide_card(card_number):
    n = card_number.split()
    n = list(''.join(n))
    for i in range(12):
        n[i] = '*'
    n = ''.join(n)
    return n


card = input()
print(hide_card(card))


# def hide_card(card_number):
#     return 12 * '*' + card_number.replace(' ', '')[-4:]
#
#
# card = input()
# print(hide_card(card))