from collections import defaultdict


def wins(pairs):
    data = defaultdict(set)
    for winner, loser in pairs:
        data[winner].add(loser)
    return data


result = wins([('Артур', 'Дима'), ('Дима', 'Артур'),
               ('Тимур', 'Элина'), ('Элина', 'Тимур'),
               ('Алина', 'Анри'), ('Анри', 'Алина')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))