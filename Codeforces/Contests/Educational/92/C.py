for _ in range(int(input())):
    n = input()
    ans = 2 * int(1e5)
    for pair in range(100):
        i = 0
        s = str(pair)
        if len(s) == 1:
            s = '0' + s
        d = 0
        for j in n:
            if j != s[i]:
                d += 1
            else:
                i = 1 - i
        if i == 1 and s[0] != s[1]:
            d += 1
        ans = min(ans, d)
    print(ans)