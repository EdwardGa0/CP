for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
    else:
        res = [[0] * n for i in range(n)]
        m = 1
        for i in range(n):
            for j in range(n):
                if not ((i+j) & 1):
                    res[i][j] = m
                    m += 1
        for i in range(n):
            for j in range(n):
                if (i+j) & 1:
                    res[i][j] = m
                    m += 1
        for i in res:
            print(*i)