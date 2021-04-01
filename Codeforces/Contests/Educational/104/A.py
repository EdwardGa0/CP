for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    res = 0
    for i in a:
        if i != m:
            res += 1
    print(res)