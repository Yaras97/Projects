import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))'))

print(timeit.timeit('"-".join(map(str, range(100)))'))

