# объявление функции
def is_password_good(password):
    bl = 0
    ml = 0
    dgt = 0
    for i in range(len(txt)):
        if ord(txt[i]) in range(65, 91):
            bl += 1
        if ord(txt[i]) in range(97, 123):
            ml += 1
        if txt[i] in "0987654321":
            dgt += 1
    if bl >= 1 and ml >= 1 and dgt >= 1 and len(txt) >= 8:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))