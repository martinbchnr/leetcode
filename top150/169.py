from typing import List
from collections import defaultdict
import numpy as np
# nums = [3,2,3]
nums = [2,2,1,1,1,1,1,2,2]


# memory-inefficient answer using a hash table that scales to lists with cardinality greater than 2
# def majorityElement(nums: List[int]):
#     freq = defaultdict(list)
#     for n in range(len(nums)):
#         freq[nums[n]].append(1)
#     for k in freq:
#         freq[k] = sum(freq[k])
#     return max(freq, key=freq.get)


# key insight: we only have lists of cardinality 2
def majorityElement(nums: List[int]):
    count = 0
    val = nums[0]
    for k in nums:
        if k == val:
            count += 1

    if count > np.floor(len(nums)/2):
        return val
    else:
        elements = set(nums)
        elements.remove(val)
        return list(elements)[0]

# best possible solutionw ith O(n) and O(1), see Boyer-Moore string-search algorithm
def majorityElement(nums: List[int]):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate=num
        
        count += (1 if num == candidate else -1) 
    return candidate

print(majorityElement(nums))
        
