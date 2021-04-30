def ints():
    return map(int, input().split())

for _ in range(int(input())):
    p, f = ints()
    cs, cw = ints()
    s, w = ints()
    ans = 0
    for i in range(cs+1):
        rem = p - i*s
        if rem < 0:
            break
        j = min(cw, rem // w)
        t1 = i + j
        ccs = cs - i
        ccw = cw - j
        if s < w:
            t2 = min(ccs, f//s)
            ff = f - t2*s
            t2 += min(ccw, ff//w)
        else:
            t2 = min(ccw, f//w)
            ff = f - t2*w
            t2 += min(ccs, ff//s)
        ans = max(ans, t1 + t2)
    print(ans)