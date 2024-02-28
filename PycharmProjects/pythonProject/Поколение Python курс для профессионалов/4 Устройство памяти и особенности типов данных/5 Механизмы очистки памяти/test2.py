import sys
nums1 = [1, 2, 3]
nums2 = nums1 + [4]
print(sys.getrefcount(nums1))