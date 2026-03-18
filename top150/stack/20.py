def isValid(s: str) -> bool:
    opening_rules = {"(": ")", 
                "{": "}", 
                "[": "]"}
    closing_rules = {v: k for k,v in opening_rules.items()}
    state = {k: 0 for k in opening_rules}
    last_opened = None
    for c in s:
        if c in opening_rules:
            if state[c] == 1 or sum(list(state.values())) > 1:
                return False
            else:
                state[c] = 1
                last_opened = c
        if c in closing_rules:
            c_inv = closing_rules[c]
            if state[c_inv] == 0:
                return False
            else:
                if c_inv == last_opened:
                    state[c_inv] = 0
                else:
                    return False
        
    return True


s = "([)]"
print(isValid(s))