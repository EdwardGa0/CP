for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    m1 = min(a)
    a.remove(m1)
    m2 = min(a)
    if m1 + m2 > d:
        if max(a) > d:
            print('NO')
        else:
            print('YES')
    else:
        print('YES')