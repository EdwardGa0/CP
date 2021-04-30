for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if k == (n-1) + (m-1)*(n):
        print('YES')
    else:
        print('NO')