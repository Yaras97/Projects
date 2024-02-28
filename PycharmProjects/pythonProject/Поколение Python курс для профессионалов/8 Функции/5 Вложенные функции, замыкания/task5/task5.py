def sort_priority(values, group):
    for i in sorted(range(len(list(group)))):
        if list(group)[i] in values:
            values[i] = list(group)[i]
    return values


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)