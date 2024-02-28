nums = {1, 2, 3}
print(nums)
id1 = id(nums)
nums |= {4}
print(nums)
id2 = id(nums)
print(id1 == id2)