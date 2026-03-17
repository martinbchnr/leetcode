def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    map_st = {}
    map_ts = {}
    # check that the constructed mapping is bijective (injective and surjective)
    for char_s, char_t in zip(s, t):
        if char_s in map_st and map_st[char_s] != char_t:
            return False
        if char_t in map_ts and map_ts[char_t] != char_s:
            return False
        
        map_st[char_s] = char_t
        map_ts[char_t] = char_s
    
    return True


s = "egg"
t = "add"

print(isIsomorphic(s,t))