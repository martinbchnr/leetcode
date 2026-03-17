
# this only works for contiguous substrings
# def isSubsequence(s: str, t: str) -> bool:
#     if len(s) > len(t):
#         return False
    
#     for i in range(len(t)-len(s)):
#         if s[i:i+len(t)] == t:
#             return True
    
#     return False

# # own approach with nested for loops
# def isSubsequence(s: str, t: str) -> bool:
#     if len(s) > len(t):
#         return False
    
#     t_idx = 0
#     counter = 0
#     for j in range(len(s)):
#         for l in range(t_idx, len(t)):
#             print(s[j], t[l])
#             if s[j] == t[l]:
#                 t_idx = l+1
#                 counter += 1
#                 break
    
#     return counter == len(s)

# use double-pointer while loops
def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    
    if len(s) == len(t):
        return s == t

    i = 0
    j = 0

    while(i < len(s)):
        while(j < len(t)):
            print(s[i], t[j])
            if(s[i] == t[j]): #if match, move to next s value
                if(i == len(s)-1):
                    return True
                j += 1
                break
            j += 1
        i += 1
    
    return False
     

# s = "abc"
# t = "ahbgdc"

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))