import sys
from time import time
sys.setrecursionlimit(10 ** 8)


def fast_exp(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k % 2 == 0:
        return fast_exp(n ** 2, k // 2)
    else:
        return n * fast_exp(n, k - 1)

# ---------------------------------------------

def GCD(a, b):  # Greatest Common Divisor
    while b != 0:
        a, b = b, a % b
    return a

# ---------------------------------------------

def Eratosphen(n):
    mas = [True] * (n + 1)
    for i in range(2, int(n ** (1/2)) + 1):
        for j in range(2 * i, n + 1, i):
            mas[j] = False
    answer = []
    for i in range(2, len(mas)):
        if mas[i]:
            answer.append(i)
    return answer


answer = Eratosphen(100)
step = 5
for i in range(0, len(answer), step):
    print(*answer[i:i + step])