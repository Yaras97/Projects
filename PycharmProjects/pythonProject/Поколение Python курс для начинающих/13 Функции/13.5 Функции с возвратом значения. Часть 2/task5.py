# объявление функции
def is_one_away(word1, word2):
    lng = 0
    if len(txt1) == len(txt2):
        if txt1 == txt2:
            return False
        for i in range(len(txt1)):
            for j in range(len(txt2)):
                if i == j:
                    if txt1[i] != txt2[j]:
                        lng += 1
        if lng > 1:
            return False
        else:
            return True

    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))