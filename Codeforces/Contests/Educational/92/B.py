def ints():
    return map(int, input().split())

for _ in range(int(input())):
    n, k, z = ints()
    a = list(ints())
    maxa = []
    for i in range(0, n-1):
        s = a[i] + a[i+1]
        if i == 0 or s > maxa[-1]:
            maxa.append(s)
        else:
            maxa.append(maxa[-1])
    maxa.append(0)
    pref = [a[0]]
    for i in a[1:]:
        pref.append(pref[-1] + i)
    res = -1
    for i in range(0, z+1):
        if k-2*i < 0:
            break
        res = max(res, pref[k-2*i] + maxa[k-2*i]*i)
    print(res)