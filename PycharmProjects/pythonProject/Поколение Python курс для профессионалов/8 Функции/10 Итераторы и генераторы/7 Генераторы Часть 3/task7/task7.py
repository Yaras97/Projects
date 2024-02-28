def unique(iterable):
    new_set = set()
    for item in iterable:
        if item not in new_set:
            new_set.add(item)
            yield item

iterator = iter('111222333')
uniques = unique(iterator)
print(next(uniques))
print(next(uniques))
print(next(uniques))