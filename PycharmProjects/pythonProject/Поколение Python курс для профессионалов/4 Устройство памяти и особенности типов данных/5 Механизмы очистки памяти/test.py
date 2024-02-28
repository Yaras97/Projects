import sys
nums = [1, 2, 3] # ссылка 1
nums1 = nums # ссылка 2
nums2 = nums1 # ссылка 3
temp = [4, 5, 6, nums] # ссылка 4, 5, 6
print(sys.getrefcount(nums)) # ссылка 7

print(nums is nums1)
print(nums1 is nums2)
print(nums is nums2)