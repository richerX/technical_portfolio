def max_len(n):
    ans = []
    for i in range(n):
        ans.append(1)
        for j in range(i):
            if mas[j] < mas[i]:
                ans[i] = max(ans[i], ans[j] + 1)
    max1 = max(ans)
    mas_ans = []
    for i in range(n - 1, -1, -1):
        if ans[i] == max1:
            mas_ans.append(mas[i])
            max1 -= 1
    mas_ans.reverse()
    return mas_ans
            
                        
n = int(input())
mas = list(map(int, input().split()))
print(*max_len(n))