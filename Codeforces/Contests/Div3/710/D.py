ans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    b = sorted(list(d.values()), reverse=True)
    if len(b) == 1:
        ans.append(n)
    else:
        x = 0
        y = 0
        l = 0
        r = 0
        for i in b:
            if x < y:
                x += i
                l += 1
            else:
                y += i
                r += 1
        if y > x:
            x, y = y, x
            l, r = r, l
        rem = x - y
        if l > 1:
            x -= rem//2
            y += rem//2
        ans.append(n - min(x, y)*2)
print(*ans)