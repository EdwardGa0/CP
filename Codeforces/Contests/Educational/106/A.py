def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, k1, k2 = read()
    w, b = read()
    maxw = min(k1, k2) + abs(k1-k2)//2
    maxb = min(n-k1, n-k2) + abs(k1-k2)//2
    if w <= maxw and b <= maxb:
        print('YES')
    else:
        print('NO')