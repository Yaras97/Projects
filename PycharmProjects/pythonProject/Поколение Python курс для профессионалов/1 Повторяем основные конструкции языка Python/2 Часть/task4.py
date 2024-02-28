lst = [int(i) for i in input().split()]
print(*sorted(filter(lambda x: lst.count(x) > 1, set(lst))))


# numbers = input().split()
# my_dict = {}
# for num in numbers:
#     my_dict[int(num)] = my_dict.get(int(num), 0) + 1
# result = [k for k, v in sorted(my_dict.items()) if v > 1]
# print(*result)