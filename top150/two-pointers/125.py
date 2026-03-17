# import re

def isPalindrome(s: str) -> bool:
    # s = re.sub('[^A-Za-z0-9]+', '', s).lower() # also works but requires additional package
    s = "".join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))