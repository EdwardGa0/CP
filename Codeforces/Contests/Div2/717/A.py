def ints():
    return map(int, input().split())

for _ in range(int(input())):
    n, k = ints()
    a = list(ints())
    for i in range(n-1):
        if k >= a[i]:
            k -= a[i]
            a[-1] += a[i]
            a[i] = 0
        else:
            a[i] -= k
            a[-1] += k
            break
    print(*a)