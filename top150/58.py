def lengthOfLastWord(s: str) -> int:
    counter = 0
    last_len = 0
    for c in s:
        if c == " ":
            counter = 0
            continue
        else:
            counter += 1
            last_len = counter

    return last_len

    


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
