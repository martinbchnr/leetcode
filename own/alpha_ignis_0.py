from collections import defaultdict

example_string = "abbca"

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
def some_function(some_string: str):
    chars = defaultdict(list)
    for k,v in enumerate(some_string):
        chars[v].append(k)
    for k, v in chars.items():
        if len(v) == 1:
            return k
        
