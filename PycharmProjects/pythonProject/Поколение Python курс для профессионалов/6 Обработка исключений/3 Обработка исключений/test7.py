data = {'Dima': [0, 4, 4, 5, 2],
        'Timur': [5, 5, 5, 5, 5],
        'Arthur': [5, 0, 4, 4, 2]}
try:
    grades = data['Arthur']
    try:
        ratio = max(grades) / min(grades)
        print(ratio)
    except (TypeError, ValueError):
        print('Произошла ошибка 2')
except KeyError:
    print('Произошла ошибка 1')
