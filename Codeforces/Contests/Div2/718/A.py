for _ in range(int(input())):
    n = int(input())
    if n % 2050 != 0:
        print(-1)
    else:
        m = n // 2050
        s = 0
        for i in str(m):
            s += int(i)
        print(s)