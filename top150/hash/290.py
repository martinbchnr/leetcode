def wordPattern(pattern: str, s: str) -> bool:
    s_split = s.split(" ")
    if len(pattern) != len(s_split):
        return False
    
    map_ps = {}
    map_sp = {}

    for (char_p, str_s) in zip(pattern, s_split):
        if char_p in map_ps and map_ps[char_p] != str_s:
            return False
        if str_s in map_sp and map_sp[str_s] != char_p:
            return False

        map_ps[char_p] = str_s
        map_sp[str_s] = char_p

    return True

pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern, s))