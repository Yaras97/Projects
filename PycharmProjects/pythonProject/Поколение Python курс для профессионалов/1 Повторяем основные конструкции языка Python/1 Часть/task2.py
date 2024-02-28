def same_parity(numbers):
    lst = []
    if numbers == []:
        return lst
    if numbers[0] % 2 == 0:
        for i in numbers:
            if i % 2 == 0:
                lst.append(i)
        return lst
    if numbers[0] % 2 != 0:
        for i in numbers:
            if i % 2 != 0:
                lst.append(i)
        return lst



# def same_parity(numbers):
#     return [i for i in numbers if i % 2 == numbers[0] % 2]


# def same_parity(numbers):
#     return list(filter(lambda elem: elem % 2 == numbers[0] % 2, numbers))