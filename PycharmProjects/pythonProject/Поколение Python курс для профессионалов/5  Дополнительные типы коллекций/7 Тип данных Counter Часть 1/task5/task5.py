from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    sign_list = list(file.read().lower())
    letters = Counter()
    for letter in sign_list:
        if letter.isalpha():
            letters.update(letter)
    [print(f'{i}: {letters[i]}') for i in sorted(letters)]
