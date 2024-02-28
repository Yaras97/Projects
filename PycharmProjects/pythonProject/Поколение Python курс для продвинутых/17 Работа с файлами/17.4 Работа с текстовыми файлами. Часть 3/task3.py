with open('input.txt', 'r+') as file:
    lst = file.readlines()

with open('output.txt', 'w') as file2:
    for i in range(len(lst)):
        print(f'{i + 1}) {lst[i]}', file=file2, end='')
