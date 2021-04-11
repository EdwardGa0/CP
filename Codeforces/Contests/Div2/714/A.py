for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > (n-1)//2:
        print(-1)
    else:
        res = []
        p = n
        for i in range(k):
            res.append(p-1)
            res.append(p)
            p -= 2
        while p >= 1:
            res.append(p)
            p -= 1
        print(*res)