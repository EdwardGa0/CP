for _ in range(int(input())):
    n, m, x = map(int, input().split())
    x -= 1
    col = x // n
    row = x % n
    print(row*m + col + 1)