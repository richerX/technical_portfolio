def eratosphen(n):
    mas = [True] * (n + 1)
    for i in range(2, int(n ** (1/2)) + 1):
        for j in range(2 * i, n + 1, i):
            mas[j] = False
    answer = []
    for i in range(2, len(mas)):
        if mas[i]:
            answer.append(i)
    return answer
