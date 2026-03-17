def isAnagram(s: str, t: str) -> bool:
    # they should have the same length since we should use original letters once again
    if len(s) != len(t):
        return False
    
    # we should not observe any unknown characters
    if set(s) != set(t):
        return False
    
    freq_s = {k: 0 for k in list(set(s))}
    freq_t = {k: 0 for k in list(set(s))}
    for char_s, char_t in zip(s, t):
        freq_s[char_s] += 1
        freq_t[char_t] += 1
    
    return list(freq_s.values()) == list(freq_t.values())


# s = "anagram"
# t = "nagaram"

s = "car"
t = "rat"
print(isAnagram(s, t))