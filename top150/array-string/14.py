from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    # check for maximum length of prefix
    prefix = ""
    prefix_len = min([len(s) for s in strs])
    if prefix_len == 0:
        return prefix
    
    for i in range(prefix_len):
        chars = set([s[i] for s in strs])
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break
    
    return prefix
    

# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))