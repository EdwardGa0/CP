for _ in range(int(input())):
    x, y = map(int, input().split())
    x = abs(x)
    y = abs(y)
    if x > y:
        x, y = y, x
    print(2*x + max(0, 2*(y-x)-1))