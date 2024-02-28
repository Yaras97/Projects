def remove_marks(text, marks, count=[]):
    count.append(1)
    remove_marks.count = len(count)
    new_lst = list(text)
    for sign in marks:
        if sign in new_lst:
            while sign in new_lst:
                new_lst.remove(sign)
    return ''.join(new_lst)


text = '-TTTTTTTtttttttRRRRRRrrrrrr-'
print(remove_marks(text, 't'))
print(remove_marks(text, 'r'))
print(remove_marks(text, 'T'))
print(remove_marks(text, 'R'))
print(remove_marks(text, '-'))
print(remove_marks.count)


# def remove_marks(text, marks):
#     if not hasattr(remove_marks, 'count'):
#         remove_marks.count = 0
#
#     remove_marks.count += 1
#     filtered_text = ''.join(char for char in text if char not in marks)
#     return filtered_text