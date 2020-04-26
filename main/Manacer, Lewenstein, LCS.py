def lcs(n):  # longest common subsequence
    ans = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if mas1[i] == mas2[j]:
                ans[i + 1][j + 1] = ans[i][j] + 1
            else:
                ans[i + 1][j + 1] = max(ans[i + 1][j], ans[i][j + 1])
    i, j = n, m
    mas_ans = []
    while i != 0 and j != 0:
        if ans[i][j] == ans[i - 1][j]:
            i -= 1
        elif ans[i][j] == ans[i][j - 1]:
            j -= 1
        else:
            mas_ans.insert(0, mas1[i - 1])
            i -= 1
            j -= 1
    return ans[n][m], mas_ans


def levenshtein_distance(a, b):
    ans = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        ans[i][0] = i
    for j in range(len(b) + 1):
        ans[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                ans[i][j] = ans[i - 1][j - 1]
            else:
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1]) + 1
    return ans[len(a)][len(b)]


def manacher(inputString):  # longest palindrom
    special_character = "#"
    s = special_character + special_character.join(list(inputString)) + special_character
    helper = [0] * len(s)
 
    c = 1
    helper[c] = 1
    r = c + helper[c]
    l = c - helper[c]
    for i in range(2, len(s)):
        # We know that the first character can't have a palindrome length > 0
        # and the second one must have a length of 1
        if helper[c - (i - c)] > (r - i) > 0:
            helper[i] = helper[c - (i - c)]
        else:
            c = i
            x = 1
            val = 0
            while (c - x) >= 0 and (c + x) < len(s):
                if s[c + x] == s[c- x]:
                    val += 1
                    x += 1
                else:
                    break
            helper[c] = val
            r = c + val
            l = c - val
    
    rl_length = max(helper)
    center = helper.index(rl_length)
    unform = s[center-rl_length:center+rl_length]
    rv = unform.replace(special_character, "")
    return rv
 
print(manacher("sdfjsadjhfsajhdfjhasfjhaseoiufyhsaeurhujrhfasaksbdjhbajdsbabbababafgasdhvgfbdsaffsnhadfsadkjfhjshdafkhskfhjas"))
