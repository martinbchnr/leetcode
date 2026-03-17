# first naive try
# def romanToInt(s: str) -> int:
#     """
#     Docstring for romanToInt
    
#     :param s: Description
#     :type s: str
#     :return: Description
#     :rtype: int
#     """
#     rom2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#     subtract_rules = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

#     year = 0
#     prev_letter = None
#     merge = False
#     for i, c in enumerate(s):
#         if merge == False:
#             if c in subtract_rules and i < len(s) - 1:
#                 merge = True
#                 prev_letter = c
#                 continue
#             else:
#                 year += rom2int[c]
#                 prev_letter = c
#         else:
#             # merge is ON
#             if prev_letter in list(subtract_rules.keys()):
#                 if c in subtract_rules[prev_letter]:
#                     # enter subtraction mode
#                     year += rom2int[c] - rom2int[prev_letter]
#                 else:
#                     year += rom2int[c] + rom2int[prev_letter]

#                 merge = False
#     return year

# own method
def romanToInt(s: str) -> int:
    """
    Docstring for romanToInt
    
    :param s: Description
    :type s: str
    :return: Description
    :rtype: int
    """
    rom2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    subtract_rules = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

    year = 0
    trail_val = None
    i = len(s) - 1
    while i >= 0:
        if trail_val is None:
            year += rom2int[s[i]]
        else:
            if s[i] in list(subtract_rules.keys()):
                if trail_val in list(subtract_rules[s[i]]):
                    year -= rom2int[s[i]]
                else:
                    year += rom2int[s[i]]
            else:
                year += rom2int[s[i]]
        trail_val = s[i]
        i -= 1
    return year

# gemini guess, which does not need the subtraction rules because it checks for monotonicity
def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        current_val = roman_map[s[i]]
        
        # Check if there is a next character and if it's larger
        if i + 1 < n and current_val < roman_map[s[i+1]]:
            total -= current_val
        else:
            total += current_val
            
    return total


# s = "MCMXCIV"
# s = "III"
# s = "LVIII"
s= "MDCCCLXXXIV"
print(romanToInt(s))