sdv, mes = int(input()), input()  #sdv - сдвиг, mes - само сообщение
for i in range(len(mes)):
    nom = ord(mes[i]) + (26 - sdv)  # nom - номер в таблице ASCII с учетом сдвига
    if 97 <= nom <= 122:  # диапазон номеров маленьких латинских букв в таблице ASCII
        print(chr(nom), end='')
    elif nom > 122:
        print(chr(nom - 26), end='')