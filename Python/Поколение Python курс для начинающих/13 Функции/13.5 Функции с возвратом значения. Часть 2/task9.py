# объявление функции
def convert_to_python_case(text):
    a = list(txt)

    for i in range(1, len(a)):
        if a[i].isupper():
            a[i] = "_" + a[i]

    b = ''.join(a).lower()
    return b

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))