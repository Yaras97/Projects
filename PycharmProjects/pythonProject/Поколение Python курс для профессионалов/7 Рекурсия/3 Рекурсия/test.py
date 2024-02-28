def recursive_sum(nums):
    if not nums:
        return 0    # базовый случай
    return nums[0] + recursive_sum(nums[1:])    # рекурсивный случай


numbers = [1, 9, 2, 8, 7, 3]
print(recursive_sum(numbers))