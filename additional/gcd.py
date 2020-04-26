def gcd(a, b):  # Greatest Common Divisor
    while b != 0:
        a, b = b, a % b
    return a
