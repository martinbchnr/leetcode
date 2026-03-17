from collections import defaultdict

# using counting-dicts, a little slower
def canConstruct(ransomNote: str, magazine: str) -> bool:
    chars = dict()
    for c in magazine:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    
    for r in ransomNote:
        if r in chars:
            if chars[r] > 0:
                chars[r] -= 1
            else:
                return False
        
        else:
            return False
    
    return True

# deleting approach using magazine as a pool (should be faster)
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for r in ransomNote:
        if r not in magazine:
            return False
        magazine = magazine.replace(r, "", 1)
        print(magazine)
    return True

ransomNote = "aba"
magazine = "ab"

print(canConstruct(ransomNote, magazine))
        
