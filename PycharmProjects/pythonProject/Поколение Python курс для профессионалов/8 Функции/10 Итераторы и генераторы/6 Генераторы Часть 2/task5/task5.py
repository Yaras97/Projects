def interleave(*args):
    max_length = max(len(seq) for seq in args)
    return (element for i in range(max_length) for seq in args for element in (seq[i],))


numbers1 = tuple(range(10))
numbers2 = list(range(10, 20))
numbers3 = tuple(range(20, 30))
numbers4 = tuple(range(30, 40))

print(*interleave(numbers1, numbers2, numbers3, numbers4))