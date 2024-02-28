from sys import getsizeof
numbers1 = range(10)
numbers2 = range(10000000)
size1 = getsizeof(numbers1)
size2 = getsizeof(numbers2)
print(size1 == size2)