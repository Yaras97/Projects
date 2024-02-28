langs = ['ru', 'mix', 'mix', 'en']
eng = 'AaBCcEeHKMOoPpTXxy'
index = sum([input() in eng for i in range(3)])
print(langs[index])



# ru = 'АаВСсЕеНКМОоРрТХху'
# letters = [input() for _ in range(3)]
# total_ru = 0
# for letter in letters:
#     total_ru += letter in ru
# print(['ru', 'mix', 'mix', 'en'][3 - total_ru])



# ru = 'АаВСсЕеНКМОоРрТХху'
# total_ru = sum(input() in ru for _ in range(3))
# print(['ru', 'mix', 'mix', 'en'][3 - total_ru])