from itertools import groupby


def group_anagrams(words):

    # Функция для создания сигнатуры слова (отсортированные буквы)
    key_func = lambda word: ''.join(sorted(word))

    # Группируем слова по их сигнатурам
    grouped_by_signature = groupby(sorted(words, key=key_func), key=key_func)

    # Создаем кортежи для каждой группы
    result = sorted(tuple(group) for key, group in grouped_by_signature)

    return result


groups = group_anagrams(['катет', 'кета'])

print(*groups)

