# импортируем тип date из модуля datetime
from datetime import date
date_day = date(2023, 9, 17)
# выводим текущую дату
print(date_day)


# print(__import__('datetime').date.today())

# from datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d'))