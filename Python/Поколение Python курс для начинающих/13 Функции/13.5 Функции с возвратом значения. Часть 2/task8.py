# объявление функции
def is_correct_bracket(text):
    s1 = txt.count('(')
    s2 = txt.count(')')
    mns = 0
    if s1 == s2:
        for i in range(len(txt)):
            if txt[0] == ')' or txt[-1] == "(":
                return False
            if txt[i] == '(':
                mns += 1
            if txt[i] == ')':
                mns -= 1
            if mns < 0:
                return False
        if mns == 0:
            return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))