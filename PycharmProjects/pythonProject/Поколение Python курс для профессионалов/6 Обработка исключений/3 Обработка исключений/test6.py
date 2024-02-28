data = {'Dima': [0, 4, 4, 5, 2],
        'Timur': [5, 5, 5, 5, 5],
        'Arthur': [3, 0, 4, 4, 3]}
try:
    grades = data['Timur']
    try:
        average = sum(grades) / len(grades)
        print(average)
    except (TypeError, ValueError):
        print('Произошла ошибка 2')
except KeyError:
    print('Произошла ошибка 1')
