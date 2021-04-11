for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(2)
        print(1, 2)
    else:
        print(2)

        print(n, n-2)
        print(n-1, n-1)
        n -= 1
        while n - 2 > 0:
            print(n, n-2)
            n -= 1