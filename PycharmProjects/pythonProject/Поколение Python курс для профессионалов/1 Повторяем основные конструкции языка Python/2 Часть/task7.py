# key_word = input()
# cnt = [i for i in range(len(key_word)) if key_word[i] in 'ауоыиэяюёе']
# for i in range(int(input())):
#     word = input()
#     count = [i for i in range(len(word)) if word[i] in 'ауоыиэяюёе']
#     if cnt == count:
#         print(word)
#     else:
#         continue


let = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
pattern = [i for i, c in enumerate(input()) if c in let]
for _ in range(int(input())):
    word = input()
    if pattern == [i for i, c in enumerate(word) if c in let]:
        print(word)