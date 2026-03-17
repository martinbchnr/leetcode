from typing import List
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

nums1 = [0]
m = 0
nums2 = [1]
n = 1

def merge(nums1, m, nums2, n):
    i = m - 1 
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        print(nums1)

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


merge(nums1, m, nums2, n)
print(nums1)
