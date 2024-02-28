def custom_isinstance(objects, typeinfo):
    return len([i for i in objects if isinstance(i, typeinfo)])


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))