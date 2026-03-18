from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    start = None
    segments = []
    prev_n = None
    for num_idx, n in enumerate(nums):
        if start is None:
            start = n 
        else:
            if n - prev_n > 1:
                if start == prev_n:
                    segments.append(f"{start}")
                else:
                    segments.append(f"{start}->{prev_n}")
                start = n

        prev_n = n
    if start == prev_n:
        segments.append(f"{start}")
    else:
        segments.append(f"{start}->{prev_n}")
    return segments

        

        

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))