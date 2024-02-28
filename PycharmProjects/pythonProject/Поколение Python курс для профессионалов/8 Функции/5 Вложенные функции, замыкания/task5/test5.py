def sort_priority(values, group):
    group_dict = {value: index for index, value in enumerate(group)}

    def priority(value):
        if value in group_dict:
            return 0, group_dict[value]
        return 1, value

    values.sort(key=priority)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)