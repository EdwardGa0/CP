for _ in range(int(input())):
    r, b, d = map(int, input().split())
    if r > b:
        r, b = b, r
    if b <= r * (d+1) and b and r:
        print('YES')
    else:
        print('NO')