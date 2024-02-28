from copy import deepcopy
data1 = [[1, 2], [3, 4]]
data2 = deepcopy(data1)
data1[0].append(10)
data2[1].append(20)
print(data1)
print(data2)