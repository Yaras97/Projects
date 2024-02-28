def reverse(sequence):
    for i in range(-1, -len(sequence) - 1, -1):
        yield sequence[i]

print(list(reverse([])))