from contextlib import redirect_stdout
with open('output.txt', mode='w', encoding='utf-8') as file:
    with redirect_stdout(file):
        print('Python generation!')
        help(len)