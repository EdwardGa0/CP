def perm(s, prev):
    if not s:
        return [0]
    for i, n in enumerate(s):
        if abs(n-prev) >= 2 and abs(n-prev) <= 4:
            res = perm(s[:i]+s[i+1:], n)
            if res:
                return [n] + res

for _ in range(int(input())):
    res = perm(list(range(1, int(input())+1)), -1)
    if res:
        print(*res[:-1])
    else:
        print(-1)