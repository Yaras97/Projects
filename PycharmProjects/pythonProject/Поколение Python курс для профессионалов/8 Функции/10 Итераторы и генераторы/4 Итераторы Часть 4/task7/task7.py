class CardDeck:
    def __init__(self):
        self.suits = ['пик', 'треф', 'бубен', 'червей']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
        # Индексы текущей карты
        self.rank_index = 0
        self.suit_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, не достигли ли конца набора карт
        if self.rank_index == len(self.ranks) and self.suit_index == len(self.suits):
            raise StopIteration

        # Формируем строку с текущей картой
        current_card = f'{self.ranks[self.rank_index]} {self.suits[self.suit_index]}'

        # Переходим к следующей карте
        self.rank_index += 1
        if self.rank_index == len(self.ranks):
            self.rank_index = 0
            self.suit_index += 1

        return current_card


cards = CardDeck()
print(next(cards))
print(next(cards))
