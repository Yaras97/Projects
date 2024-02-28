# n = int(input())
# numbers = range(1, n + 1)
# d = dict()
#
# for num in numbers:
#     sum_num = sum([int(digit) for digit in str(num)])
#     d.setdefault(sum_num, []).append(num)
#
# print(max(map(len, d.values())))


numbers = list(range(1, int(input()) + 1))
numbers = list(map(str, numbers))
my_dict = [sum([int(total) for total in num]) for num in numbers]
my_dict = [my_dict.count(i) for i in my_dict]
print(max(my_dict))


# my_dict = {}
# for i in range(1, int(input()) + 1):
#     total_num = sum(map(int, str(i)))
#     my_dict[total_num] = my_dict.get(total_num, 0) + 1
# print(max(my_dict.values()))
