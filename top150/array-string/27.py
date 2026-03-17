from typing import List
nums = [0,1,2,2,3,0,4,2] # [3,2,2,3] / [0,1,2,2,3,0,4,2]
val = 2 # 3 / 5 

# Input: nums = , val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

# def removeElement(nums: List[int], val: int) -> int:
#     k = 0
#     i = 0
#     l = len(nums)
#     while i < len(nums):
#         print("i", nums[i])
#         if nums[i] == val:
            
#             while l >= i:
#                 k += 1
#                 print("l", nums[l])
#                 if nums[l] != val:
                    
#                     nums[i] = nums[l]
#                     nums[l] = val
#                     break
#                 else:
#                     l -= 1
#         i += 1
#         print("done", nums)
#     return k, nums

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    k = len(nums) - 1  
    while i <= k:
        if nums[i] == val:
            nums[i] = nums[k]
            nums[k] = val
            k -= 1
        else:
            i += 1
            
    return i

def removeElement(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1

    return n, nums
            
print(removeElement(nums, val))