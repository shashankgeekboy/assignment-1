def increment_integer(digits):
    
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digit = digits[i] + carry
        if digit == 10:
            digit = 0
            carry = 1
        else:
            carry = 0
            digits[i] = digit

    if carry:
        digits.append(1)

    return digits
digits = [1, 2, 3]
result = increment_integer(digits)
print(result)
