res = []

for _ in range(int(input())):
    n = int(input())
    x = 0
    t = 0
    instruc = []
    xt = [(0, 0)]
    for i in range(n):
        ti, xi = map(int, input().split())
        instruc.append([ti, xi])
        if ti >= t:
            t = max(ti, t) + abs(xi - x)
            x = xi
            xt.append((t, x))
    suc = 0
    idx = 0
    for i in range(n-1):
        t1, x1 = instruc[i]
        t2, x2 = instruc[i+1]
        while not (xt[idx][0] <= t1 and xt[idx+1] >= t2):
            idx += 1
        