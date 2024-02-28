import sys
nums1 = [1, 2, 3]
nums2 = nums1
nums3 = [nums1, nums2]
del nums1
print(sys.getrefcount(nums2))