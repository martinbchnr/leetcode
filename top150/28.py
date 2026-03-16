import time
# first try, when i was not aware of the fact that you might need to restart within a traversal
# def strStr(haystack: str, needle: str) -> int:
#     index = -1
#     n_idx = 0
#     for i, s in enumerate(haystack):
#         print(n_idx)
#         if n_idx < len(needle):
#             if s == needle[n_idx]:
#                 if n_idx == 0:
#                     index = i
#                 n_idx += 1
                
#             else:
#                 if n_idx == len(needle):
#                     return index # found needle
#                 else:
#                     index = -1
#                     n_idx = 0
    
#     return index if n_idx == len(needle) else -1

# haystack = "leetcode"
# needle = "leeto"

# newer and working method
# def strStr(haystack: str, needle: str) -> int:
#     index = -1
#     n_idx = 0
#     for i, s in enumerate(haystack):
#         while n_idx < len(needle):
#             print(haystack[i:i+n_idx+1], needle[:n_idx+1])
#             if haystack[i:i+n_idx+1] == needle[:n_idx+1]:
#                 n_idx += 1
#                 if n_idx == len(needle):
#                     return i # found needle
#             else:
#                 break
#             time.sleep(1)    
#     return index


# best solution: not doing it iteratively over the needle indices but globally
def strStr(haystack: str, needle: str) -> int:
    index = -1
    n_idx = 0
    for i, s in enumerate(haystack):
        if haystack[i:i+len(needle)] == needle:
            return i
    return index



haystack = "mississippi"
needle = "issip"

print(strStr(haystack, needle))
            
