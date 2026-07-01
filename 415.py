def addStrings(num1: str, num2: str) -> str:
    # prepend zeros to ensure equal length
    len1, len2 = len(num1), len(num2)
    if len1 < len2:
        diff = len2 - len1
        num1 = "0"*diff + num1
    elif len2 < len1:
        diff = len1 - len2
        num2 = "0"*diff + num2
    
    print(num1, num2)

    carry = 0
    # start from the rightmost digit towards the left
    total = ""
    for idx in range(len(num1)-1, -1, -1):
        print("idx", idx)
        curr_sum = int(num1[idx]) + int(num2[idx]) + carry
        print("curr_sum", curr_sum)
        curr_digit = curr_sum % 10
        print("carry", carry)
        carry = curr_sum // 10
        print("curr_digit", curr_digit)
        total = str(curr_digit) + total
    
    if carry != 0:
        total = str(carry) + total
    
    return total

if __name__ == "__main__":
    num1 = "11"
    num2 = "123"
    print(addStrings(num1, num2))        