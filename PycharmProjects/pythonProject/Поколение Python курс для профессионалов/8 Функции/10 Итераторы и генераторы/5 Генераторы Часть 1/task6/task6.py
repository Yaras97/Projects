def card_deck(suit):
    suits = ['пик', 'треф', 'бубен', 'червей']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    suits.remove(suit)
    while True:
        for i in suits:
            for j in ranks:
                yield f'{j} {i}'


generator = card_deck('пик')

cards = [next(generator) for _ in range(80)]

print(*cards)