from typing import List

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums: List[int]) -> int:
    # my own solution
    # if not nums:
    #     return 0
    
    # k = 1
    # i = 0
    # j = i + 1
    # while j <= len(nums) - 1:
    #     val = nums[i]
    #     if nums[j] <= val:
    #         j += 1
    #     else:
    #         nums[i+1] = nums[j]
    #         k += 1
    #         i += 1
    #         j = i
    # print(nums)
    # return k

    # alternative with for loop
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
    
    

print(removeDuplicates(nums))

