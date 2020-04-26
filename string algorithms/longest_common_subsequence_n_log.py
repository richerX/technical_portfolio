def lower_bound(mas, p):
    l, r = 0, len(mas)
    while r - l > 0:
        mid = (r + l) // 2
        if mas[mid] < p:
            l = mid + 1
        else:
            r = mid
    return l


INF = 10 ** 10 
n, a1, k, b, m = map(int, input().split()) 
mas = [a1] 
for i in range(0, n - 1): 
    mas.append((k * mas[i] + b) % m) 
dp = [INF for i in range(n + 1)] 
dp[0] = -INF 
p = [-1 for i in range(n + 1)] 
pch = [-1 for i in range(n)]  
 

for i in range(n): 
    j = lower_bound(dp, mas[i]) 
    if dp[j - 1] < mas[i] and mas[i] < dp[j]: 
        dp[j] = mas[i] 
        pch[i] = p[j - 1] 
        p[j] = i 

dpindex = -1 
for i in range(n, -1, -1): 
    if dp[i] != INF: 
        dpindex = i 
        break 
index = p[dpindex] 
ans = [] 
while index != -1: 
    ans.append(mas[index]) 
    index = pch[index] 
ans.reverse() 
print(' '.join(map(str, ans)))