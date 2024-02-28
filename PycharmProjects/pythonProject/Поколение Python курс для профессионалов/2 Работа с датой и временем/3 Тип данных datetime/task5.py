from datetime import datetime
text = 'Дорогой дневник, 11.02.2021 произошло нечто невероятное. На часах было 18:09..'
pattern = 'Дорогой дневник, %d.%m.%Y произошло нечто невероятное. На часах было %H:%M..'
dt = datetime.strptime(text, pattern)
print(dt)
