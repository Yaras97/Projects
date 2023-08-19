with open('file.txt') as file:
    file = file.read()
    words = file.split()
    lst = ''.join(i if i.isalpha() else ' ' for i in file)
    letters = list(filter(str.isalpha, lst))
    count = 1
    for i in file:
        if '\n' in i:
            count += 1

    print(f'Input file contains:\n'
          f'{len(letters)} letters\n'
          f'{len(words)} words\n'
          f'{count} lines')