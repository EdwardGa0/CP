def read():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = read()
    res = []
    t = 1
    for i in a:
        while t <= i/2:
            t <<= 1
        while t >= i*1.5:
            t >>= 1
        res.append(t)
    print(*res)
        