from typing import List

def isHappy(n: int) -> bool:
    if isinstance(n, int) and n > 0:
        digits = str(n)
        seen = []
        while int(digits) != 1:
            digits = str(sum([int(d)**2 for d in digits]))
            print(digits)
            if digits in seen:
                return False
            seen.append(digits)
        return True
    else:
        return False

print(isHappy(2))