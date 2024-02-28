def linear(nested_lists):
    if not nested_lists:
        return list()
    new_list = list()
    for i in nested_lists:
        if type(i) is list:
            new_list.extend(linear(i))
        else:
            new_list.append(i)
    return new_list


my_list = [[123], 23, 43, 65, 754, 3, 1, 2]

print(linear(my_list))