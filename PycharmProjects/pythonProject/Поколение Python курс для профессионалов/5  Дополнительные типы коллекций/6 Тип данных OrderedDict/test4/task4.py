from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values is False:
        for key in sorted(ordered_dict.keys()):
            ordered_dict.move_to_end(key)
        return ordered_dict
    elif by_values is True:
        for key, value in sorted(ordered_dict.items(), key=lambda x: x[1]):
            ordered_dict.move_to_end(key)
        return ordered_dict


data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items())