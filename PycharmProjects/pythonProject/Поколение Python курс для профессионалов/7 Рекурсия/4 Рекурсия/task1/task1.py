def recursive_sum(nested_lists):
    if nested_lists == list():
        return 0
    c = 0
    for i in nested_lists:
        if type(i) is list:
            c += recursive_sum(i)
        else:
            c += i
    return c


my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
