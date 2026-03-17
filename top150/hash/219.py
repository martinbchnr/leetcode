from typing import List
from collections import defaultdict

# uses hashing
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Docstring for containsNearbyDuplicate
    
    constraints: nums[i] == nums[j] and abs(i - j) <= k.

    :param self: Description
    :param nums: Description
    :type nums: List[int]
    :param k: Description
    :type k: int
    :return: Description
    :rtype: bool
    """

    n_idcs = defaultdict(list)
    for n_idx, n in enumerate(nums):
        if n in n_idcs:
            for prev_idx in n_idcs[n]:
                if abs(n_idx - prev_idx) <= k:
                    return True
        n_idcs[n].append(n_idx)
    return False

# potentially faster with just window-based eval
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # catch case with no duplicates
    if len(nums) == len(set(nums)):
        return False
    else:
        for i in range(len(nums)):
            if nums[i] in nums[i+1 : i+k+1]:
                return True

nums = [1,2,3,0,1]
k = 3
print(containsNearbyDuplicate(nums, k))