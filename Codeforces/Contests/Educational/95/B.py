for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ul = []
    for i, e in enumerate(l):
        if e == 0:
            ul.append(a[i])
    ul.sort(reverse=True)
    it = 0
    for i, e in enumerate(l):
        if e == 0:
            a[i] = ul[it]
            it += 1
    print(*a)