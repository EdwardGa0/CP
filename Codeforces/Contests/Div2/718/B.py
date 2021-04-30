def ints():
    return map(int, input().split())

for _ in range(int(input())):
    n, m = ints()
    s = []
    for i in range(n):
        for j in ints():
            s.append([j, i])
    s.sort()
    res = [[0] * m for i in range(n)]
    for i in range(m):
        res[s[i][1]][i] = s[i][0]
    for i in range(m, n*m):
        for j in range(m):
            if not res[s[i][1]][j]:
                res[s[i][1]][j] = s[i][0]
                break
    for row in res:
        print(*row)
