'''
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует
символы в строке согласно следующим правилам:
все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.
Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и
вывести полученный результат.
'''


def stupid_sorted(number):
    low_letter = ''
    up_letter = ''
    odd = ''
    even = ''
    for sym in number:
        if sym in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
            low_letter += sym
        if sym in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
            up_letter += sym
        if sym.isdigit():
            if int(sym) % 2 == 1:
                odd += sym
            if int(sym) % 2 == 0:
                even += sym
    return ''.join(sorted(low_letter) + sorted(up_letter) + sorted(odd) + sorted(even))


print(stupid_sorted('3DYrz34UXl'))
