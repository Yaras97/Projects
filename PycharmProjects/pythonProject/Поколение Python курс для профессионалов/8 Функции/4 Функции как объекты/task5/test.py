def remove_marks(text, marks):
    if not hasattr(remove_marks, 'count'):
        remove_marks.count = 0

    remove_marks.count += 1
    filtered_text = ''.join(char for char in text if char not in marks)
    return filtered_text


text = '!Hi!!!! Will we ????go together?????'

print(remove_marks(text, '!?'))
print(remove_marks.count)

