slv = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
n = input() + ' запретил букву'
for i in slv:
    if i not in n:
        continue
    print(n, i)
    if i in n:
        while i in n:
            n = n.replace(i, '').replace('  ', ' ').lstrip().strip()