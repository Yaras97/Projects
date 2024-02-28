letters = 'abcdefghijklmnopqrstuvwxyz'
new_dict = input()
sentence = input().lower()
table = sentence.maketrans(letters, new_dict)
print(sentence.translate(table))