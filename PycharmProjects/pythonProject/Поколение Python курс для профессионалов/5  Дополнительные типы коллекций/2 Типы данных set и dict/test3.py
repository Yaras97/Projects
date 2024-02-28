my_set = set()
for i in range(3):
    my_set.add(i + 1)
    my_set.discard(i - 1)
print(my_set)
print(len(my_set))

