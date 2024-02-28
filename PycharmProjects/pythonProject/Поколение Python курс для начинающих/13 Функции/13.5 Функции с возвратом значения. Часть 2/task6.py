# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i not in (',.!?- ')]
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))