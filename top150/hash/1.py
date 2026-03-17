from typing import List

# for-loop based function (probably more memory efficient)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

# function based on hashing
def twoSum(nums: List[int], target: int) -> List[int]:
    prefix = {}
    for index, no in enumerate(nums):
        if (target - no) in prefix:
            return [prefix[target-no], index]
        prefix[no] = index
    return []




nums = [7, 5, 12]
target = 12
print(twoSum(nums, target))