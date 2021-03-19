import math

for _ in range(int(input())):
    n = int(input())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    d = list(map(int, input().split()))

    prev = 0
    ans = 0
    for i in range(n):
        a, b = t[i]
        ans += a - prev + d[i]
        if i < n-1:
            ans = max(b, ans + math.ceil((b-a)/2))
        prev = b
    print(ans)