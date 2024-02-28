from datetime import date


def date_formatter(country_code):
    country = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y', 'fr': '%d.%m.%Y',
               'pt': '%d-%m-%Y'}

    def func(date):
        return date.strftime(country[country_code])

    return func


date_ru = date_formatter('pt')
today = date(2025, 1, 5)
print(date_ru(today))
