with open(input(), encoding='utf-8') as file, open('forbidden_words.txt', encoding='utf-8') as words:
    wr_words = words.read().split()
    for i in file:
        for k in wr_words:
            while k in i.lower():
                index = i.lower().index(k)
                i = i[:index] + '*' * len(k) + i[index + len(k):]
        print(i.strip())